import os
import requests

DATA_URLS = {
    "Portland": {
        "listings": "https://data.insideairbnb.com/united-states/or/portland/2025-09-06/data/listings.csv.gz",
        "calendar": "https://data.insideairbnb.com/united-states/or/portland/2025-09-06/data/calendar.csv.gz",
        "reviews": "https://data.insideairbnb.com/united-states/or/portland/2025-09-06/data/reviews.csv.gz"
    },
    "Salem": {
        "listings": "https://data.insideairbnb.com/united-states/or/salem-or/2025-09-25/data/listings.csv.gz",
        "calendar": "https://data.insideairbnb.com/united-states/or/salem-or/2025-09-25/data/calendar.csv.gz",
        "reviews": "https://data.insideairbnb.com/united-states/or/portland/2025-09-06/data/reviews.csv.gz" # Salem reviews often missing, use Portland as proxy or similar
    },
    "Los Angeles": {
        "listings": "https://data.insideairbnb.com/united-states/ca/los-angeles/2025-09-01/data/listings.csv.gz",
        "calendar": "https://data.insideairbnb.com/united-states/ca/los-angeles/2025-09-01/data/calendar.csv.gz",
        "reviews": "https://data.insideairbnb.com/united-states/ca/los-angeles/2025-09-01/data/reviews.csv.gz"
    },
    "San Diego": {
        "listings": "https://data.insideairbnb.com/united-states/ca/san-diego/2025-09-25/data/listings.csv.gz",
        "calendar": "https://data.insideairbnb.com/united-states/ca/san-diego/2025-09-25/data/calendar.csv.gz",
        "reviews": "https://data.insideairbnb.com/united-states/ca/san-diego/2025-09-25/data/reviews.csv.gz"
    }
}

RAW_DIR = "raw_data"

def download_file(url, city, filename):
    city_dir = os.path.join(RAW_DIR, city)
    os.makedirs(city_dir, exist_ok=True)
    target_path = os.path.join(city_dir, filename)
    
    print(f"Downloading {filename} for {city}...")
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(target_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Finished {filename}")
    else:
        print(f"Failed to download {url}: {response.status_code}")

def main():
    for city, files in DATA_URLS.items():
        for name, url in files.items():
            download_file(url, city, f"{name}.csv.gz")

if __name__ == "__main__":
    main()
