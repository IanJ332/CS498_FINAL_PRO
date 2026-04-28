import os
import time
from pymongo import MongoClient
from google.cloud import bigquery
from google.oauth2 import service_account
from dotenv import load_dotenv

load_dotenv()

# Config
MONGO_URI = os.getenv("MONGO_URI")
BQ_KEY_FILE = "final-492902-b95cff0ffa0e.json"
PROJECT_ID = "final-492902"

mongo_client = MongoClient(MONGO_URI)
db = mongo_client.get_default_database()

bq_creds = service_account.Credentials.from_service_account_file(BQ_KEY_FILE)
bq_client = bigquery.Client(credentials=bq_creds, project=PROJECT_ID)

def measure(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution Time: {end - start:.4f}s")
        return result
    return wrapper

@measure
def run_q1():
    print("\n--- [Query 1] MongoDB - Portland 2-Day Search ---")
    pipeline = [
        {"$match": {"date": {"$in": ["2026-02-23", "2026-02-24"]}, "available": True}},
        {"$group": {"_id": "$listing_id", "price": {"$avg": "$price"}, "days": {"$sum": 1}}},
        {"$match": {"days": 2}},
        {"$lookup": {"from": "listings", "localField": "_id", "foreignField": "id", "as": "info"}},
        {"$unwind": "$info"},
        {"$match": {"info.city": "Portland"}},
        {"$project": {"_id": 0, "name": "$info.name", "price": 1, "rating": "$info.review_scores_rating"}},
        {"$sort": {"rating": -1}},
        {"$limit": 3}
    ]
    results = list(db.calendar.aggregate(pipeline))
    for r in results: print(r)

@measure
def run_q2():
    print("\n--- [Query 2] MongoDB - Portland 'No Vacancy' Areas ---")
    # All neighborhoods in Portland
    all_nb = db.listings.distinct("neighbourhood_cleansed", {"city": "Portland"})
    # Neighborhoods with ANY availability in March
    available_nb = db.calendar.aggregate([
        {"$match": {"date": {"$regex": "^2026-03"}, "available": True, "city": "Portland"}},
        {"$lookup": {"from": "listings", "localField": "listing_id", "foreignField": "id", "as": "info"}},
        {"$unwind": "$info"},
        {"$group": {"_id": "$info.neighbourhood_cleansed"}}
    ])
    available_list = [r["_id"] for r in available_nb]
    no_vacancy = [nb for nb in all_nb if nb not in available_list]
    print(f"Found {len(no_vacancy)} areas with no vacancy: {no_vacancy[:5]}")

@measure
def run_q3():
    print("\n--- [Query 3] MongoDB - Salem 3-Night Booking ---")
    pipeline = [
        {"$match": {"date": {"$in": ["2026-03-01", "2026-03-02", "2026-03-03"]}, "available": True}},
        {"$group": {"_id": "$listing_id", "avg_price": {"$avg": "$price"}, "days": {"$sum": 1}}},
        {"$match": {"days": 3}},
        {"$lookup": {"from": "listings", "localField": "_id", "foreignField": "id", "as": "info"}},
        {"$unwind": "$info"},
        {"$match": {"info.city": "Salem"}},
        {"$project": {"_id": 0, "name": "$info.name", "avg_price": 1}},
        {"$limit": 3}
    ]
    results = list(db.calendar.aggregate(pipeline))
    for r in results: print(r)

@measure
def run_q4():
    print("\n--- [Query 4] MongoDB - Amenity Regex Search ---")
    results = list(db.listings.find(
        {"city": "Portland", "review_scores_rating": {"$gte": 4.8}, "amenities": {"$regex": "Wifi", "$options": "i"}},
        {"_id": 0, "name": 1, "rating": "$review_scores_rating"}
    ).sort("rating", -1).limit(3))
    for r in results: print(r)

@measure
def run_q5():
    print("\n--- [Query 5] BigQuery - Historical Review Trends ---")
    sql = """
        SELECT city, EXTRACT(YEAR FROM CAST(date AS DATE)) as year, COUNT(*) as count
        FROM `final-492902.airbnb_raw.reviews`
        WHERE date LIKE '%-12-%'
        GROUP BY city, year
        ORDER BY count DESC LIMIT 3
    """
    results = [dict(row) for row in bq_client.query(sql).result()]
    for r in results: print(r)

@measure
def run_q6():
    print("\n--- [Query 6] BigQuery - Market Distribution ---")
    sql = """
        SELECT 
            city, 
            COUNT(*) as total_listings,
            ROUND(AVG(SAFE_CAST(REGEXP_REPLACE(price, r'[^0-9.]', '') AS FLOAT64)), 2) as avg_price
        FROM `final-492902.airbnb_raw.listings`
        GROUP BY city
        ORDER BY total_listings DESC
    """
    results = [dict(row) for row in bq_client.query(sql).result()]
    for r in results: print(r)

if __name__ == "__main__":
    run_q1()
    run_q2()
    run_q3()
    run_q4()
    run_q5()
    run_q6()
