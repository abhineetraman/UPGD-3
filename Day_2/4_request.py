import requests

data = requests.get(url="http://api.open-notify.org/iss-now.json", headers={"User-Agent":"Nasa"})

print(data.text)