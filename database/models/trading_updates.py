# trading_updates.py
from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from db.manager import Base


class TradingUpdate(Base):
    __tablename__ = 'trading_updates'

    id = Column(Integer, primary_key=True, autoincrement=True)
    message_id = Column(Integer, ForeignKey('messages.id'))
    total_trades = Column(Integer, nullable=False)
    successful_trades = Column(Integer, nullable=False)
    unsuccessful_trades = Column(Integer, nullable=False)
    profit_percentage = Column(Float, nullable=False)

    message = relationship('Message', back_populates='trading_updates')
