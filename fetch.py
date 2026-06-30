import json
import requests
from datetime import datetime, timezone
from pathlib import Path

# สร้าง data.json ถ้ายังไม่มี
if not Path("data.json").exists():
    Path("data.json").write_text("{}", encoding="utf-8")

# สร้าง history.json ถ้ายังไม่มี
if not Path("history.json").exists():
    Path("history.json").write_text("[]", encoding="utf-8")


URL = "https://production.dataviz.cnn.io/index/fearandgreed/graphdata"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=HEADERS, timeout=30)
response.raise_for_status()

data = response.json()

fg = data["fear_and_greed"]

result = {
    "updated": datetime.now(timezone.utc).isoformat(),
    "score": fg["score"],
    "rating": fg["rating"],
    "previous_close": fg["previous_close"],
    "previous_1_week": fg["previous_1_week"],
    "previous_1_month": fg["previous_1_month"],
    "previous_1_year": fg["previous_1_year"]
}

with open("data.json", "w", encoding="utf8") as f:
    json.dump(result, f, indent=4)

history_file = Path("history.json")

if history_file.exists():
    history = json.loads(history_file.read_text())
else:
    history = []

history.append(result)

history = history[-1000:]

history_file.write_text(
    json.dumps(history, indent=4),
    encoding="utf8"
)

print(result)
