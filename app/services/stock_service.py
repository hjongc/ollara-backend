from sqlalchemy.orm import Session
from ..models.stock import Stock
from ..models.stock_price import StockPrice
from ..models.stock_prediction import StockPrediction
from datetime import date

def update_stock_price(db: Session, stock_symbol: str, stock_data: dict):
    stock = db.query(Stock).filter(Stock.symbol == stock_symbol).first()
    if not stock:
        stock = Stock(symbol=stock_symbol, name=stock_data['name'])
        db.add(stock)
        db.commit()
        db.refresh(stock)

    new_price = StockPrice(
        stock_id=stock.id,
        date=date.today(),
        open=stock_data['open'],
        close=stock_data['close'],
        high=stock_data['high'],
        low=stock_data['low'],
        volume=stock_data['volume']
    )
    db.add(new_price)
    db.commit()
    return new_price

def get_latest_stock_prices(db: Session):
    return db.query(StockPrice).filter(StockPrice.date == date.today()).all()

def save_stock_prediction(db: Session, stock_id: int, prediction_value: float):
    prediction = StockPrediction(
        stock_id=stock_id,
        date=date.today(),
        prediction_value=prediction_value
    )
    db.add(prediction)
    db.commit()
    return prediction
