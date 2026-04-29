import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url=os.getenv("NVIDIA_BASE_URL"),
    api_key=os.getenv("NVIDIA_API_KEY")
)

def get_mql_from_ai(user_input):
    """
    Converts natural language to a MongoDB aggregation pipeline using NVIDIA NIM.
    """
    system_prompt = """
    You are an expert MongoDB Data Architect. Your task is to convert English natural language questions into MongoDB Aggregation Pipelines (MQL).
    
    COLLECTION SCHEMA:
    1. 'listings':
       - id (int)
       - name (string)
       - city (string): Portland, Salem, Los Angeles, San Diego
       - neighbourhood_cleansed (string): Neighborhood name
       - room_type (string): e.g. 'Entire home/apt'
       - accommodates (int)
       - price (float): Numeric value
       - review_scores_rating (float): 0-5
       - amenities (string): e.g. '["Wifi", "Kitchen"]' (use $regex to search)
    
    2. 'calendar':
       - listing_id (int)
       - date (string): YYYY-MM-DD
       - available (boolean)
       - price (float)

    RULES:
    - Return ONLY the JSON array for the pipeline.
    - Do not include markdown code blocks (```json ... ```).
    - If the user asks for a search involving dates or availability, start with the 'calendar' collection and use $lookup to join 'listings'.
    - If the user asks for listing attributes (amenities, city, rating), query the 'listings' collection.
    - Always use $limit to restrict results to 50 for performance.
    - Ensure field names match the schema exactly (e.g. use neighbourhood_cleansed not neighborhood).
    - For search queries, project fields: name, neighborhood (from neighbourhood_cleansed), price, and rating.
    """

    try:
        response = client.chat.completions.create(
            model=os.getenv("NVIDIA_MODEL"),
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Generate a MongoDB aggregation pipeline for: {user_input}"}
            ],
            temperature=0.1,
            max_tokens=1024
        )
        
        pipeline_str = response.choices[0].message.content.strip()
        
        # Clean up potential markdown formatting if LLM ignores rules
        if pipeline_str.startswith("```"):
            pipeline_str = pipeline_str.split("\n", 1)[1].rsplit("\n", 1)[0]
        if pipeline_str.startswith("json"):
            pipeline_str = pipeline_str[4:].strip()
            
        return json.loads(pipeline_str)
    except Exception as e:
        print(f"AI Service Error: {e}")
        return None
