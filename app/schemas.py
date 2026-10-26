from pydantic import BaseModel, HttpUrl
from datetime import datetime

class News(BaseModel):
  title: str
  url: HttpUrl
  image_url: HttpUrl | None = None
  summary: str | None = None
  published_at: datetime | None = None
  updated_at: datetime | None = None