from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def setup_engine(db_url: str = 'sqlite:///test.db') -> Engine:
    engine = create_engine(db_url)

    return engine


def start_session(engine: Engine) -> Session:
    session = sessionmaker(bind=engine)

    return session()


def end_session(session: Session) -> None:
    session.close()


def create_tables(engine: Engine) -> None:
    Base.metadata.create_all(bind=engine)
