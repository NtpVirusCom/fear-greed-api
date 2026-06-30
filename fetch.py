from playwright.sync_api import sync_playwright
import json

URL = "https://edition.cnn.com/markets/fear-and-greed"

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=True
    )

    page = browser.new_page(
        viewport={"width":1600,"height":900}
    )

    page.goto(
        URL,
        wait_until="networkidle",
        timeout=120000
    )

    page.screenshot(path="page.png")

    html = page.content()

    print(html[:1000])

    browser.close()
