from fastapi import FastAPI
from app.routes import router

app = FastAPI(
  title="G1 API",
  description="API de notícias do G1",
  version="0.1.1"
)

app.include_router(router)