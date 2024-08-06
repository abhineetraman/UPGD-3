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

# Loop to collect 100 records
for _ in range(100):
    # Make a request to the API
    response = requests.get(url, headers={"User-Agent": "Nasa"})
    
    # Load the JSON response
    js_data = json.loads(response.text)
    
    # Extract the required data
    timestamp = js_data['timestamp']
    latitude = js_data['iss_position']['latitude']
    longitude = js_data['iss_position']['longitude']
    message = js_data['message']
    
    # Append the data to the records list
    records.append({
        "timestamp": timestamp,
        "latitude": latitude,
        "longitude": longitude,
        "message": message
    })
    
    # Wait for a second before making the next request to avoid hitting the API rate limit
    time.sleep(1)

# Convert the records list to a DataFrame
df = pd.DataFrame(records)

# Write the DataFrame to a CSV file
df.to_csv("iss_location_data.csv", index=False)

print("Data has been written to iss_location_data.csv")
