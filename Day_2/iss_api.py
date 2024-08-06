import requests
import json

data = requests.get(url="http://api.open-notify.org/iss-now.json", headers={"User-Agent":"Nasa"})

js_data = json.loads(data.text)

print(f"timestamp: {js_data['timestamp']}, \nLatitude: {js_data['iss_position']['latitude']}, \nLongitude: {js_data['iss_position']['longitude']}")