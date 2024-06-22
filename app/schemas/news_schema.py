from pydantic import BaseModel
from typing import List
from datetime import datetime

class NewsSummary(BaseModel):
    title: str
    summary: str
    source: str

class NewsUpdateResult(BaseModel):
    status: str
    message: str
    updated_at: datetime
