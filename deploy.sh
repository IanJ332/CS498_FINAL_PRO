#!/bin/bash

# Ensure we exit on any error
set -e

PROJECT_ID="final-492902"
SERVICE_NAME="airbnb-backend"
REGION="us-central1" # Feel free to change region as needed

echo "Deploying the Flask backend to Google Cloud Run..."

# Deploy using gcloud run deploy
gcloud run deploy $SERVICE_NAME \
  --source . \
  --project $PROJECT_ID \
  --region $REGION \
  --allow-unauthenticated \
  --set-env-vars "GCP_PROJECT_ID=${PROJECT_ID}"

echo "Deployment complete!"
