import typing as t
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

from app.core import config

engine = create_engine(
    config.SQLALCHEMY_DATABASE_URI,
    pool_size=20, max_overflow=5
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Dependency
def get_db() -> t.Iterator[Session]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
