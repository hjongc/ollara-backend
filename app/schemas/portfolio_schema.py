from pydantic import BaseModel
from typing import List

class PortfolioTips(BaseModel):
    total_value: float
    performance: float

class PortfolioAnalysisResult(BaseModel):
    total_value: float
    risk_level: str
    stock_performance: List[dict]
