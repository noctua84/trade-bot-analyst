from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime

from db.manager import Base


class Amount(Base):
    __tablename__ = 'amounts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Float, nullable=False)
    currency = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.now, nullable=False)
