from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import json

URL = "https://edition.cnn.com/markets/fear-and-greed"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto(URL, wait_until="networkidle")

    html = page.content()

    browser.close()

soup = BeautifulSoup(html, "html.parser")

print(soup.title.text)

# หา element ที่มีคะแนน Fear & Greed
# (ต้องตรวจสอบ selector จริงอีกครั้ง เพราะ CNN เปลี่ยนโครงสร้างได้)

score = None
rating = None

data = {
    "score": score,
    "rating": rating
}

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
