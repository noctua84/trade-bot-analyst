from sqlalchemy import Column, Integer, ForeignKey, DateTime, TIMESTAMP
from sqlalchemy.orm import relationship
from datetime import datetime

from db.manager import Base


class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, autoincrement=True)
    message_id = Column(Integer, ForeignKey('messages.id'), nullable=False)
    timestamp = Column(TIMESTAMP, nullable=False)
    bot_id = Column(Integer, ForeignKey('bots.id'), nullable=False)

    created_at = Column(DateTime, default=datetime.now, nullable=False)

    bot = relationship("Bot", back_populates="messages")
    account_updates = relationship(
        "AccountUpdate",
        back_populates="message",
        cascade="all, delete-orphan",
        order_by="AccountUpdate.id"
    )
    trading_updates = relationship(
        "TradingUpdate",
        back_populates="message",
        cascade="all, delete-orphan",
        order_by="TradingUpdate.id"
    )
