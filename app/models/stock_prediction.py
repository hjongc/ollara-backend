from sqlalchemy import Column, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from ..core.database import Base

class StockPrediction(Base):
    __tablename__ = "stock_predictions"

    id = Column(Integer, primary_key=True, index=True)
    stock_id = Column(Integer, ForeignKey('stocks.id'))
    date = Column(Date)
    prediction_value = Column(Float)

    stock = relationship("Stock", back_populates="predictions")
