from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from db.manager import Base


class Bot(Base):
    __tablename__ = 'bots'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    created_at = Column(DateTime, default=datetime.now, nullable=False)

    messages = relationship('Message', back_populates='bot', order_by='Message.id', cascade='all, delete-orphan')
    strategies = relationship('Strategy', back_populates='bot', order_by='Strategy.id')
