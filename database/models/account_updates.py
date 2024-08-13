from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship

from db.manager import Base


class AccountUpdate(Base):
    __tablename__ = 'account_updates'

    id = Column(Integer, primary_key=True, autoincrement=True)
    message_id = Column(Integer, ForeignKey('messages.id'))
    balance_id = Column(Integer, ForeignKey('amounts.id'))
    withdrawal_id = Column(Integer, ForeignKey('amounts.id'))
    income = Column(Float, nullable=True)

    message = relationship('Message', back_populates='account_updates')
    balance = relationship('Amount', foreign_keys='AccountUpdate.balance_id')
    withdrawal = relationship('Amount', foreign_keys='AccountUpdate.withdrawal_id')
    strategies = relationship('Strategy', secondary='strategy_status', back_populates='account_updates')
