from fastapi import APIRouter, Query
from app.services import get_cached_news, search_news

router = APIRouter()

@router.get("/")
def home():
  return {
    "name": "g1 API",
    "version": "0.1.2",
    "status": "online"
  }

@router.get("/health")
def health_check():
  return {"status": "ok"}

@router.get("/news")
def news(limit: int = Query(10, ge=1, le=20)):
  return get_cached_news()[:limit]

@router.get("/news/search")
def search(q: str, limit: int = Query(10, ge=1, le=20)):
  return search_news(q)[:limit]