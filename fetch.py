import json
import requests

URL = "https://production.dataviz.cnn.io/index/fearandgreed/graphdata"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(URL, headers=headers)

data = r.json()

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
