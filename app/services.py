from app.scraper import get_news
from time import time

_cache = {
  "news": None,
  "expires_at": 0
}
cache_ttl = 60

def get_cached_news():
  now = time()

  if _cache["news"] is not None and now < _cache["expires_at"]:
    return _cache["news"]

  news = get_news(limit=20)
  _cache["news"] = news
  _cache["expires_at"] = now + cache_ttl

  return news

  
def search_news(query: str, limit: int = 10):
  news = get_cached_news()
  query = query.casefold()

  return [
    article
    for article in news
    if query in article.title.casefold()
  ]