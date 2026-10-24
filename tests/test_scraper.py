from app.scraper import get_news

news = get_news()

print(f"Noticías encontradas: {len(news)}")

for newspaper in news[:10]:
  print(newspaper["title"])
  print(newspaper["url"])
  print("-" * 60)