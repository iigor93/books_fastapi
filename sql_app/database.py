from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, DeclarativeBase

SQLALCHEMY_DB_URL = "sqlite:///./sql_app.db"
engine = create_engine(SQLALCHEMY_DB_URL, connect_args={"check_same_thread": False})


class Base(DeclarativeBase):
    pass


# Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


def get_db():
    with Session(engine) as session:
        return session


DB_SESSION = Annotated[Session, Depends(get_db)]
