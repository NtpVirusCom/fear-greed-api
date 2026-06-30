import requests

URL = "https://production.dataviz.cnn.io/index/fearandgreed/graphdata"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(URL, headers=headers)

print(r.status_code)
print(r.headers.get("content-type"))
print(r.text[:1000])
