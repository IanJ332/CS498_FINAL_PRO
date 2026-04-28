# Airbnb Data Pipeline & Analytics (CS498 Final Project)

This project implements a high-performance, dual-source data pipeline for Airbnb market analysis across four US cities (Portland, Salem, Los Angeles, San Diego).

## 🚀 Architecture Overview
To balance real-time performance and deep analytical depth, we utilize a **Lambda-style Architecture**:

1.  **MongoDB (Hot Layer):** Stores operational data (Listings metadata + Q1/Q2 2026 availability). Optimized for < 500ms dashboard queries.
2.  **BigQuery (Analytical Layer):** Stores the full 1.4GB raw dataset (20M+ rows). Used for historical trends and city-wide market distribution.

## 🛠️ Setup Instructions

### 1. Prerequisites
- Python 3.10+
- MongoDB Atlas Account (Free Tier)
- Google Cloud Project with BigQuery enabled

### 2. Local Environment Setup
```bash
# Clone the repo
git clone git@github.com:IanJ332/CS498_FINAL_PRO.git
cd CS498_FINAL_PRO

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Environment Variables (.env)
Create a `.env` file in the root directory with the following content:
```env
MONGO_URI=your_mongodb_connection_string
GCP_PROJECT_ID=final-492902
GOOGLE_APPLICATION_CREDENTIALS=path_to_your_gcp_json_key.json
```

4. Running the Backend
```bash
python app.py
```
The server will start at `http://localhost:8080`.

### 5. Running the Frontend
Since the frontend is a single-page application (SPA):
- **Option A:** Simply open `frontend/index.html` in your browser.
- **Option B (Recommended):** Serve it using Python:
```bash
python -m http.server 3000 --directory frontend
```
Then visit `http://localhost:3000`.

## 📊 Available APIs
- `GET /api/dashboard/portland_search`: Q1 - Fast Portland 2-day availability.
- `GET /api/dashboard/amenities`: Q4 - High-rated listings with Wifi.
- `GET /api/analysis/review_trends`: Q5 - Historical review growth (via BigQuery).
- `GET /api/analysis/market_stats`: Q6 - City-wide average prices (via BigQuery).

## 📄 Documentation
- See `Current_DB_Status_Report.md` for the full query audit and data validation samples.

## 👥 Contributors
- IanJ332
