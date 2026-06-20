import requests
import time
from bs4 import BeautifulSoup

TOKEN = "BURAYA_TOKEN_YAZ"
CHAT_ID = "6187060345"

URL = "https://turbo.az/autos?q%5Bmake%5D%5B%5D=toyota&q%5Bmodel%5D%5B%5D=highlander&q%5Byear_from%5D=2021&q%5Bfuel_type%5D%5B%5D=hybrid"

seen = set()

def send(msg):
    requests.get(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        params={"chat_id": CHAT_ID, "text": msg}
    )

def check():
    r = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(r.text, "html.parser")

    ads = soup.select("a.products-i__link")

    for ad in ads:
        link = ad.get("href")
        if not link:
            continue

        full = "https://turbo.az" + link
        title = ad.text.strip()

        if full not in seen:
            seen.add(full)
            send("🚗 Yeni elan!\n\n" + title + "\n" + full)

while True:
    check()
    time.sleep(60)
