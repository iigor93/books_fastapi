from fastapi import FastAPI, HTTPException, Request, Body

from sql_app.database import engine, DB_SESSION

from user_profile import models as user_profile_models
from user_profile import crud as user_profile_crud
from user_profile import schemas as user_profile_schemas

from books import models as books_models
from books import crud as books_crud
from books import schemas as books_schemas


user_profile_models.Base.metadata.create_all(bind=engine)
books_models.Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.get("/user_profile/{user_profile_id}/", response_model=user_profile_schemas.UserProfile)
def get_user_profile(db: DB_SESSION, user_profile_id: int = 1):
    user_profile = user_profile_crud.get_user_profile(db)
    return user_profile


@app.put("/user_profile/{user_profile_id}/")  #, response_model=user_profile_schemas.UserProfile)
def update_user_profile(db: DB_SESSION, request: str = Request):  # user_profile: user_profile_schemas.UserProfile, user_profile_id: int = 1):
    print(request)
    # user_profile_updated = user_profile_crud.update_user_profile(db, user_profile)
    return "OK"  # user_profile_updated


""" BOOKS """


@app.get("/books/")
def get_books_list(db: DB_SESSION) -> list[books_schemas.Book | None]:
    books_list: list[books_schemas.Book] | None = books_crud.get_books_list(db)
    return books_list


@app.post("/books/", response_model=books_schemas.Book)
def create_book(book: books_schemas.Book, db: DB_SESSION):
    return books_crud.create_book(db, book=book)


@app.get("/books/{book_id}", response_model=books_schemas.Book)
def get_book(db: DB_SESSION, book_id: int = 1):
    book = books_crud.get_book(db, book_id=book_id)
    return book


@app.put("/books/{book_id}", response_model=books_schemas.Book)
def update_book(book_id: int, book: books_schemas.Book, db: DB_SESSION):
    return books_crud.update_book(db, book_id=book_id, book=book)


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int, db: DB_SESSION):
    if books_crud.delete_book(db, book_id=book_id):
        return {"detail": "Book deleted"}
    raise HTTPException(status_code=404, detail="Not found")

#
# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: DB_SESSION):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already exists")
#     return crud.create_user(db, user=user)
#
#
# async def common_parameters(skip: Annotated[int, Query(le=7)] = 1, q: str | None = None, limit: int = 100):
#     return {"q": q, "skip": skip, "limit": limit}
#
#
# COMMON_DEP = Annotated[dict, Depends(common_parameters)]
#
#
# async def one_more_common_parameters(skip_one: Annotated[int, Query(le=7)] = 1):
#     return skip_one + 56
#
#
# class Dep:
#     def __init__(self, skip_one: str):
#         self.skip_one = skip_one
#
#
# class PydanticItem(BaseModel):
#     name: str
#
#
# SECOND_DEP = Annotated[PydanticItem, Depends()]
#
#
# @app.get("/")
# async def get_test(commons: COMMON_DEP,
#                    second: Annotated[int, Depends(one_more_common_parameters)],
#                    name: SECOND_DEP):
#     print(commons)
#     commons.update({"second": second})
#     if name.name:
#         commons.update({"name": name.name})
#     return commons

