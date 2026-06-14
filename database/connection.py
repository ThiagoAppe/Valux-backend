import os
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase


DatabaseUrl = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://postgres:password@localhost:5432/valux"
)


class Base(DeclarativeBase):
    pass


Engine = create_engine(
    DatabaseUrl,
    pool_pre_ping=True,
)


SessionFactory = sessionmaker(
    bind=Engine,
    autoflush=False,
    autocommit=False,
)


def GetDb() -> Generator[Session, None, None]:
    Db = SessionFactory()

    try:
        yield Db
    finally:
        Db.close()