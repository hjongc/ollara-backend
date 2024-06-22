from pydantic import BaseModel
from typing import List

class TrendingStock(BaseModel):
    symbol: str
    name: str
    trending_score: int

class StockSearchResult(BaseModel):
    symbol: str
    name: str

class StockAnalysisResult(BaseModel):
    symbol: str
    prediction: float
    related_news: List[str]
    chart_data: List[dict]
