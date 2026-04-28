# Use the official Python 3.9 slim image
FROM python:3.9-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Set the working directory
ENV APP_HOME /app
WORKDIR $APP_HOME

# Copy local code to the container image
COPY . ./

# Install production dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080
EXPOSE 8080

# Run the web service on container startup using gunicorn
# 1 worker process and 8 threads
# Timeout is set to 0 to disable timeouts of workers to allow Cloud Run to handle scaling
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
