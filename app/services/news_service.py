from sqlalchemy.orm import Session
from ..models.news import News
from datetime import datetime

def get_news_summary(db: Session):
    return db.query(News).all()

def update_news(db: Session):
    news = News(title="Market Update", summary="Stocks are up...", source="Bloomberg", updated_at=datetime.utcnow())
    db.add(news)
    db.commit()
    return {
        "status": "success",
        "message": "News updated successfully",
        "updated_at": news.updated_at
    }
