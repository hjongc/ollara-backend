from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, date
from sqlalchemy.orm import Session
from ..services.stock_service import update_stock_price, get_latest_stock_prices, save_stock_prediction
from ..dependencies.database import get_db
from ..core.database import SessionLocal
import random

def fetch_stock_data():
    # 예시로 랜덤 데이터를 반환
    return {
        "symbol": "AAPL",
        "name": "Apple Inc.",
        "open": random.uniform(150, 160),
        "close": random.uniform(150, 160),
        "high": random.uniform(160, 170),
        "low": random.uniform(140, 150),
        "volume": random.randint(1000000, 5000000)
    }

def update_and_predict():
    db: Session = SessionLocal()
    stock_data = fetch_stock_data()
    update_stock_price(db, stock_data["symbol"], stock_data)

    # 머신러닝 예측 모델을 사용하여 예측 값을 생성하는 로직
    latest_prices = get_latest_stock_prices(db)
    for price in latest_prices:
        prediction_value = random.uniform(150, 160)  # 여기에 실제 예측 모델 적용
        save_stock_prediction(db, price.stock_id, prediction_value)

scheduler = BackgroundScheduler()
scheduler.add_job(update_and_predict, 'cron', hour=0)  # 매일 00시에 실행
scheduler.start()
