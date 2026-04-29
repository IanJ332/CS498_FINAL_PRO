import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url=os.getenv("NVIDIA_BASE_URL"),
    api_key=os.getenv("NVIDIA_API_KEY")
)

def get_query_from_ai(user_input):
    """
    Intelligently decides between MongoDB (Operational) and BigQuery (Analytical).
    Returns a JSON object: { "engine": "mongo"|"bigquery", "query": <MQL_Array>|<SQL_String>, "target": <collection_name> }
    """
    system_prompt = """
    You are a Hybrid Data Architect for an Airbnb Dashboard. You must decide whether to use MongoDB (for real-time, specific search) or BigQuery (for historical, city-wide analysis).

    SCHEMA CONTEXT:
    1. MongoDB ('listings' & 'calendar'): Best for specific searches, availability, ratings, and listing attributes.
       - 'listings' fields: name, city, neighbourhood_cleansed, room_type, price, review_scores_rating, amenities (string).
       - ROOM_TYPE MAPPING: 
         * 'apartment', 'house', 'studio', 'full home' -> 'Entire home/apt'
         * 'private room', 'single room' -> 'Private room'
         * 'shared room', 'hostel' -> 'Shared room'
         * 'hotel' -> 'Hotel room'
       - 'calendar' fields: listing_id, date, available (bool), price.
    2. BigQuery (Full paths: 'final-492902.airbnb_raw.listings' & 'final-492902.airbnb_raw.reviews'): Best for historical trends, year-over-year growth, and massive city-level stats.
       - Use 'final-492902.airbnb_raw.listings' for city stats and prices. (Note: Use SAFE_CAST(REGEXP_REPLACE(price, r'[$,]', '') AS FLOAT64) for average price calculations).
       - Use 'final-492902.airbnb_raw.reviews' for date-based analysis.

    DECISION RULES:
    - Use 'mongo' for: "Find rooms in...", "Available next week", "Wifi in Portland", "Cheapest stays".
    - Use 'bigquery' for: "Review trends over time", "Growth of listings in...", "Market distribution", "Historical prices".

    OUTPUT FORMAT:
    Return ONLY a JSON object. No markdown, no explanations.
    - For Mongo: { "engine": "mongo", "query": [ <aggregation_stages> ], "target": "listings"|"calendar" }
    - For BigQuery: { "engine": "bigquery", "query": "SELECT ...", "target": "analytical" }

    LIMITS: Always add LIMIT 50. 
    In BigQuery, if you use 'GROUP BY', all non-grouped columns in SELECT must be inside an aggregate function like AVG() or SUM().
    EXAMPLE BIGQUERY: {"engine": "bigquery", "query": "SELECT city, AVG(SAFE_CAST(REGEXP_REPLACE(price, r'[$,]', '') AS FLOAT64)) as avg_price FROM `final-492902.airbnb_raw.listings` GROUP BY city LIMIT 50"}
    In Mongo, ALWAYS add a stage {"$project": {"_id": 0, "name": 1, "neighborhood": "$neighbourhood_cleansed", "price": 1, "rating": "$review_scores_rating"}} or similar to ensure '_id' is excluded and fields are correctly mapped.
    """

    try:
        response = client.chat.completions.create(
            model=os.getenv("NVIDIA_MODEL"),
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=0.1
        )
        
        content = response.choices[0].message.content.strip()
        
        # Clean potential markdown
        if content.startswith("```"):
            content = content.split("\n", 1)[1].rsplit("\n", 1)[0]
        if content.startswith("json"):
            content = content[4:].strip()
            
        return json.loads(content)
    except Exception as e:
        print(f"AI Service Error: {e}")
        return None
