from sqlalchemy import Integer, ForeignKey, Column, Table

from db.manager import Base

strategy_status = Table(
    'strategy_status', Base.metadata,
    Column('strategy_id', Integer, ForeignKey('strategies.id'), primary_key=True),
    Column('account_update_id', Integer, ForeignKey('account_updates.id'), primary_key=True),
)
