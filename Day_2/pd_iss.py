import pandas as pd
import requests
import json
import time

# URL of the ISS location API
url = "http://api.open-notify.org/iss-now.json"

# Create an empty DataFrame with the required columns
df = pd.DataFrame(columns=["timestamp", "latitude", "longitude", "message"])

# List to collect all the records before converting to a DataFrame
records = []

# Function to get ISS location data
def get_iss_data():
    response = requests.get(url, headers={"User-Agent": "Nasa"}, timeout=10)
    js_data = json.loads(response.text)
    timestamp = js_data['timestamp']
    latitude = js_data['iss_position']['latitude']
    longitude = js_data['iss_position']['longitude']
    message = js_data['message']
    return {
        "timestamp": timestamp,
        "latitude": latitude,
        "longitude": longitude,
        "message": message
    }

# Loop to collect 100 records
attempt = 0
max_attempts = 10

while len(records) < 100 and attempt < max_attempts:
    try:
        record = get_iss_data()
        records.append(record)
        print(f"Record {len(records)} collected")
        time.sleep(1)  # Wait before the next request to avoid hitting the API rate limit
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}. Retrying in {2 ** attempt} seconds...")
        time.sleep(2 ** attempt)  # Exponential backoff
        attempt += 1

# Convert the records list to a DataFrame
df = pd.DataFrame(records)

# Write the DataFrame to a CSV file
df.to_csv("iss_location_data.csv", index=False)

print("Data has been written to iss_location_data.csv")
