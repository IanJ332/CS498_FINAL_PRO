import os
import pandas as pd
import gzip
from pymongo import MongoClient, UpdateOne
from google.cloud import bigquery
from google.oauth2 import service_account
from dotenv import load_dotenv

load_dotenv()

# Config
MONGO_URI = os.getenv("MONGO_URI")
BQ_KEY_FILE = "final-492902-b95cff0ffa0e.json"
CITIES = ["Portland", "Salem", "Los Angeles", "San Diego"] 
RAW_DIR = "raw_data"
MONGO_CALENDAR_MONTHS = ["2026-02", "2026-03"] 

# Init DBs
mongo_client = MongoClient(MONGO_URI)
db = mongo_client.get_default_database()

bq_creds = service_account.Credentials.from_service_account_file(BQ_KEY_FILE)
bq_client = bigquery.Client(credentials=bq_creds, project=bq_creds.project_id)
BQ_DATASET = "airbnb_raw"

def clean_price(price_str):
    if pd.isna(price_str) or price_str == "":
        return 0.0
    try:
        return float(str(price_str).replace("$", "").replace(",", ""))
    except:
        return 0.0

def process_city(city):
    print(f"--- Processing {city} ---")
    city_dir = os.path.join(RAW_DIR, city)
    
    # 1. Process Listings
    listings_path = os.path.join(city_dir, "listings.csv.gz")
    print("Reading listings...")
    df_listings = pd.read_csv(listings_path, compression='gzip', low_memory=False)
    df_listings['city'] = city
    
    # Clean prices for MongoDB and mapping
    df_listings['price_num'] = df_listings['price'].apply(clean_price)
    
    # Create price map for calendar fallback
    price_map = df_listings.set_index('id')['price_num'].to_dict()
    
    # Prepare for MongoDB (subset of fields)
    mongo_listings = df_listings[[
        'id', 'name', 'neighbourhood_cleansed', 'room_type', 
        'accommodates', 'review_scores_rating', 'city', 'amenities', 'price_num'
    ]].copy()
    mongo_listings.rename(columns={'price_num': 'price'}, inplace=True)
    
    print(f"Syncing {len(mongo_listings)} listings to MongoDB...")
    ops = [UpdateOne({'id': row['id']}, {'$set': row.to_dict()}, upsert=True) for _, row in mongo_listings.iterrows()]
    db.listings.bulk_write(ops)
    
    # Sync to BigQuery (Full data) - Force all columns to string to avoid schema mismatch
    df_listings_bq = df_listings.astype(str)
    job_config = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")
    bq_client.load_table_from_dataframe(df_listings_bq, f"{BQ_DATASET}.listings", job_config=job_config).result()

    # 2. Process Calendar
    calendar_path = os.path.join(city_dir, "calendar.csv.gz")
    print(f"Reading calendar for {city}...")
    chunk_size = 1000000
    bq_jobs = []
    for chunk in pd.read_csv(calendar_path, compression='gzip', chunksize=chunk_size, low_memory=False):
        chunk['city'] = city
        chunk['price_num'] = chunk['price'].apply(clean_price)
        chunk['available_bool'] = chunk['available'].map({'t': True, 'f': False})
        
        # Fallback to listing price if calendar price is missing or 0 (Vectorized)
        chunk['price_num'] = chunk['price_num'].where(chunk['price_num'] > 0, chunk['listing_id'].map(price_map).fillna(0.0))
        
        # MongoDB: Pruning to stay under 512MB
        # 1. Only Available: True
        # 2. Only next few months (Feb/March/April 2026)
        mask = (chunk['available_bool'] == True) & (chunk['date'].str.startswith(tuple(MONGO_CALENDAR_MONTHS)))
        mongo_calendar = chunk[mask][['listing_id', 'date', 'available_bool', 'price_num', 'city']].copy()
        mongo_calendar.rename(columns={'available_bool': 'available', 'price_num': 'price'}, inplace=True)
        
        # Batch insert to MongoDB
        if not mongo_calendar.empty:
            db.calendar.insert_many(mongo_calendar.to_dict('records'))
        
        # BigQuery: Sync full chunk (Asynchronous) - Force string
        chunk_bq = chunk.astype(str)
        job_config = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")
        job = bq_client.load_table_from_dataframe(chunk_bq, f"{BQ_DATASET}.calendar", job_config=job_config)
        bq_jobs.append(job)
        print(f"Dispatched calendar chunk to BQ...")

    # 3. Process Reviews
    reviews_path = os.path.join(city_dir, "reviews.csv.gz")
    print(f"Reading reviews for {city}...")
    for chunk in pd.read_csv(reviews_path, compression='gzip', chunksize=chunk_size, low_memory=False):
        chunk['city'] = city
        
        # MongoDB: We SKIP raw reviews to save space. Q5 should go to BigQuery.
        # But if you REALLY want them, we could store city-year-month aggregates.
        
        # BigQuery: Sync full chunk (Asynchronous) - Force string
        job_config = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")
        chunk_bq = chunk.astype(str)
        job = bq_client.load_table_from_dataframe(chunk_bq, f"{BQ_DATASET}.reviews", job_config=job_config)
        bq_jobs.append(job)
        print(f"Dispatched reviews chunk to BQ...")
    
    # Wait for all jobs in this city to finish
    print(f"Waiting for {len(bq_jobs)} BQ jobs to finish for {city}...")
    for job in bq_jobs:
        job.result()

def main():
    # Clear existing collections for clean start
    print("Clearing MongoDB collections...")
    db.listings.drop()
    db.calendar.drop()
    db.reviews.drop()
    
    # Create BigQuery dataset if not exists
    dataset = bigquery.Dataset(f"{bq_client.project}.{BQ_DATASET}")
    dataset.location = "US"
    try:
        bq_client.create_dataset(dataset, exists_ok=True)
    except Exception as e:
        print(f"Dataset might already exist: {e}")

    # Overwrite BQ tables for clean start
    # Note: load_table_from_dataframe with WRITE_TRUNCATE on first city, then APPEND
    
    # Create Indices for performance
    print("Creating MongoDB indices...")
    db.listings.create_index([("id", 1)], unique=True)
    db.listings.create_index([("city", 1)])
    db.calendar.create_index([("listing_id", 1), ("date", 1)])
    db.calendar.create_index([("city", 1)])
    db.reviews.create_index([("listing_id", 1)])
    db.reviews.create_index([("date", 1)])
    
    first = True
    for city in CITIES:
        # For the very first load of the very first city, we truncate to ensure a clean start
        # Wait, if I use WRITE_TRUNCATE inside process_city, it will wipe previous cities.
        # So I need to handle it here.
        if first:
            # Drop tables to ensure schema is fresh
            bq_client.delete_table(f"{BQ_DATASET}.listings", not_found_ok=True)
            bq_client.delete_table(f"{BQ_DATASET}.calendar", not_found_ok=True)
            bq_client.delete_table(f"{BQ_DATASET}.reviews", not_found_ok=True)
            first = False
            
        process_city(city)

if __name__ == "__main__":
    main()
