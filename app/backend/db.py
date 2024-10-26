from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
engine = create_engine('sqlite:///taskmanager.db', echo=True)   # создание движока указав пусть в БД
SessionLocal = sessionmaker(bind=engine)    # локальная сессия


class Base(DeclarativeBase):
    pass
