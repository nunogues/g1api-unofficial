
import requests
from bs4 import BeautifulSoup

from app.scraper import get_news



for news in get_news(limit=1):
    print(news.model_dump_json(indent=2))

    
    response = requests.get(
        str(news.url),
        timeout=10,
        headers={"User-Agent": "G1API/0.1"}
    )
    response.raise_for_status()

    
    soup = BeautifulSoup(response.text, "html.parser")

    print("\n--- METADADOS DE DATA ---")

    for tag in soup.find_all("meta"):
        key = (
            tag.get("name")
            or tag.get("property")
            or tag.get("itemprop")
            or ""
        )

        if "date" in key.lower():
            print(tag.attrs)
