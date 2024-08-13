from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship

from db.manager import Base


class Strategy(Base):
    __tablename__ = 'strategies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    active = Column(Boolean, nullable=False, default=True)
    bot_id = Column(Integer, ForeignKey('bots.id'), nullable=False)

    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=True, default=None, onupdate=datetime.now)

    bot = relationship('Bot', back_populates='strategies')
    account_updates = relationship('AccountUpdate', secondary='strategy_status', back_populates='strategy')