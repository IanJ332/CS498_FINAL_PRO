import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from google.cloud import bigquery
from google.oauth2 import service_account
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# --- Configuration ---
MONGO_URI = os.getenv("MONGO_URI")
BQ_KEY_FILE = "final-492902-b95cff0ffa0e.json"
BQ_DATASET = "airbnb_raw"
PROJECT_ID = "final-492902"

# --- DB Connections ---
mongo_client = MongoClient(MONGO_URI)
db = mongo_client.get_default_database()

# Use service account for BQ
if os.path.exists(BQ_KEY_FILE):
    bq_creds = service_account.Credentials.from_service_account_file(BQ_KEY_FILE)
    bq_client = bigquery.Client(credentials=bq_creds, project=PROJECT_ID)
else:
    bq_client = bigquery.Client(project=PROJECT_ID)

@app.route('/')
def health_check():
    return jsonify({"status": "healthy", "service": "Airbnb Hybrid Backend"}), 200

# --- Dashboard API (MongoDB - Hot Data) ---

@app.route('/api/dashboard/portland_search')
def dashboard_portland():
    """Q1: Portland 2-Day Search (Feb 23-24, 2026) - Fast Mongo Version"""
    pipeline = [
        {"$match": {"date": {"$in": ["2026-02-23", "2026-02-24"]}, "available": True}},
        {"$group": {"_id": "$listing_id", "price": {"$avg": "$price"}, "days": {"$sum": 1}}},
        {"$match": {"days": 2}},
        {"$lookup": {"from": "listings", "localField": "_id", "foreignField": "id", "as": "info"}},
        {"$unwind": "$info"},
        {"$match": {"info.city": "Portland"}},
        {"$project": {
            "_id": 0, "id": "$_id", "name": "$info.name", 
            "neighborhood": "$info.neighbourhood_cleansed", 
            "room_type": "$info.room_type", "accommodates": "$info.accommodates", 
            "price": {"$ifNull": ["$price", 0]}, 
            "rating": {"$ifNull": ["$info.review_scores_rating", 0]}
        }},
        {"$sort": {"rating": -1}},
        {"$limit": 50}
    ]
    return jsonify(list(db.calendar.aggregate(pipeline)))

@app.route('/api/dashboard/amenities')
def dashboard_amenities():
    """Q4: Wifi + High Rating Search"""
    pipeline = [
        {"$match": {"city": "Portland", "review_scores_rating": {"$gte": 4.8}, "amenities": {"$regex": "Wifi", "$options": "i"}}},
        {"$project": {
            "_id": 0, "id": 1, "name": 1, 
            "neighborhood": "$neighbourhood_cleansed", 
            "room_type": 1, 
            "rating": {"$ifNull": ["$review_scores_rating", 0]}
        }},
        {"$sort": {"rating": -1}},
        {"$limit": 50}
    ]
    return jsonify(list(db.listings.aggregate(pipeline)))

@app.route('/api/dashboard/no_vacancy')
def dashboard_no_vacancy():
    """Optimized: Show Top 5 Neighborhoods with HIGHEST Booking Occupancy for March 2026"""
    pipeline = [
        {"$match": {"date": {"$regex": "^2026-03"}, "available": False}},
        {"$group": {"_id": "$listing_id", "booked_days": {"$sum": 1}}},
        {"$lookup": {"from": "listings", "localField": "_id", "foreignField": "id", "as": "details"}},
        {"$unwind": "$details"},
        {"$group": {"_id": "$details.neighbourhood_cleansed", "total_booked": {"$sum": "$booked_days"}}},
        {"$sort": {"total_booked": -1}},
        {"$limit": 10},
        {"$project": {"_id": 0, "neighborhood": "$_id", "booked_count": "$total_booked"}}
    ]
    return jsonify(list(db.calendar.aggregate(pipeline)))

@app.route('/api/dashboard/salem_booking')
def dashboard_salem():
    """Q3: Salem 3-Night Booking (March 1-3, 2026)"""
    pipeline = [
        {"$match": {"date": {"$in": ["2026-03-01", "2026-03-02", "2026-03-03"]}, "available": True}},
        {"$group": {"_id": "$listing_id", "avg_price": {"$avg": "$price"}, "days": {"$sum": 1}}},
        {"$match": {"days": 3}},
        {"$lookup": {"from": "listings", "localField": "_id", "foreignField": "id", "as": "details"}},
        {"$unwind": "$details"},
        {"$match": {"details.city": "Salem"}},
        {"$project": {
            "_id": 0, "name": "$details.name", 
            "neighborhood": "$details.neighbourhood_cleansed", 
            "room_type": "$details.room_type", "accommodates": "$details.accommodates",
            "price": {"$ifNull": ["$avg_price", 0]}
        }}
    ]
    return jsonify(list(db.calendar.aggregate(pipeline)))

# --- Deep Dive API (BigQuery - Cold Data) ---

@app.route('/api/details/listing/<int:listing_id>')
def listing_details(listing_id):
    """Fetch FULL history and details for a specific listing from BigQuery"""
    query = f"""
        SELECT * FROM `{PROJECT_ID}.{BQ_DATASET}.listings`
        WHERE id = {listing_id}
    """
    try:
        results = [dict(row) for row in bq_client.query(query)]
        return jsonify(results[0] if results else {"error": "Not found"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/analysis/review_trends')
def review_trends():
    """Q5: Historical Review Trends (Joined with Listings to get City)"""
    query = f"""
        SELECT 
            COALESCE(l.city, 'Unknown') as city, 
            COALESCE(EXTRACT(YEAR FROM SAFE.PARSE_DATE('%Y-%m-%d', r.date)), 0) as year, 
            COUNT(*) as review_count
        FROM `{PROJECT_ID}.{BQ_DATASET}.reviews` r
        JOIN `{PROJECT_ID}.{BQ_DATASET}.listings` l ON r.listing_id = l.id
        WHERE EXTRACT(MONTH FROM SAFE.PARSE_DATE('%Y-%m-%d', r.date)) = 12
        GROUP BY city, year
        ORDER BY city, year DESC
        LIMIT 50
    """
    try:
        results = [dict(row) for row in bq_client.query(query)]
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/analysis/market_stats')
def market_stats():
    """Q6: Market Analysis by Neighborhood"""
    query = f"""
        SELECT 
            COALESCE(city, 'Unknown') as city, 
            COALESCE(neighbourhood_cleansed, 'Unknown') as neighborhood, 
            COUNT(*) as total_listings,
            COALESCE(ROUND(AVG(SAFE_CAST(REGEXP_REPLACE(price, r'[$,]', '') AS FLOAT64)), 2), 0) as avg_price
        FROM `{PROJECT_ID}.{BQ_DATASET}.listings`
        GROUP BY city, neighborhood
        ORDER BY total_listings DESC
        LIMIT 50
    """
    try:
        results = [dict(row) for row in bq_client.query(query)]
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
