
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

start_url = "https://g1.globo.com/"

def get_news():
    response = requests.get(
        start_url,
        timeout=10,
        headers={"User-Agent": "G1API/0.1"}
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.select("a.feed-post-link")

    news = []

    for link in links:

      title = link.get_text(" ", strip=True)
      href = link.get("href")
  
      if not title or not href:
            continue

      url = urljoin(start_url, href)

      news.append({
            "title": title,
            "url": url
        })

    return news
