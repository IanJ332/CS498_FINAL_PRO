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

### 3. Configuration & Credentials
1.  **Environment Variables**: Copy `.env.example` to `.env` and fill in your keys.
    ```bash
    cp .env.example .env
    ```
2.  **GCP Credentials**: Place your Google Cloud Service Account JSON key in the root directory and name it: `final-492902-b95cff0ffa0e.json`.

### 4. Running the Project
1.  **Start Backend**:
    ```bash
    python app.py
    ```
    The server will start at `http://localhost:8080`.

2.  **Start Frontend**:
    Open `frontend/index.html` directly, or serve it:
    ```bash
    python -m http.server 3000 --directory frontend
    ```

## 🪄 AI Magic Search
The dashboard now features an **AI Intelligent Search** bar. 
- It uses **NVIDIA NIM (Llama 3.1 8B)** to interpret natural language.
- It automatically decides whether to query **MongoDB** (for specific, real-time listing info) or **BigQuery** (for massive historical trends).

## 📄 Documentation
- See `Current_DB_fix_Report.md` for the latest database query audit results and data validation.
- See `presentation_prompts.md` for recommended AI queries to use during the demo.

## 👥 Contributors
- IanJ332 & Team
