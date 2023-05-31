from typing import Annotated

from fastapi import FastAPI, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy.orm import Session

from sql_app import crud, models, schemas
from sql_app.database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already exists")
    return crud.create_user(db, user=user)


async def common_parameters(skip: Annotated[int, Query(le=7)] = 1, q: str | None = None, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


COMMON_DEP = Annotated[dict, Depends(common_parameters)]


async def one_more_common_parameters(skip_one: Annotated[int, Query(le=7)] = 1):
    return skip_one + 56


class Dep:
    def __init__(self, skip_one: str):
        self.skip_one = skip_one


class PydanticItem(BaseModel):
    name: str


SECOND_DEP = Annotated[PydanticItem, Depends()]


@app.get("/")
async def get_test(commons: COMMON_DEP,
                   second: Annotated[int, Depends(one_more_common_parameters)],
                   name: SECOND_DEP):
    print(commons)
    commons.update({"second": second})
    if name.name:
        commons.update({"name": name.name})
    return commons

