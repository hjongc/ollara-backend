from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class NewsSummary(BaseModel):
    title: str
    summary: str
    source: str

@router.get("/home/news-summary", response_model=List[NewsSummary])
async def get_news_summary():
    return [
        {"title": "Market Update", "summary": "Stocks are up...", "source": "Bloomberg"},
        ...
    ]
