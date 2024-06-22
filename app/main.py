from fastapi import FastAPI
from .api.v1.endpoints import prediction, portfolio, news
from .core.database import engine, Base
from .utils.scheduler import scheduler

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(prediction.router, prefix="/api/v1", tags=["Prediction"])
app.include_router(portfolio.router, prefix="/api/v1", tags=["Portfolio"])
app.include_router(news.router, prefix="/api/v1", tags=["News"])

# 애플리케이션 시작 시 스케줄러 시작
scheduler.start()
