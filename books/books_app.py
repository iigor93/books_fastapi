from fastapi import APIRouter, HTTPException

from books import crud as books_crud
from books import schemas as books_schemas
from sql_app.database import DB_SESSION

router = APIRouter()


@router.get("/")
def get_books_list(db: DB_SESSION) -> list[books_schemas.Book | None]:
    books_list: list[books_schemas.Book] | None = books_crud.get_books_list(db)
    return books_list


@router.post("/", response_model=books_schemas.Book)
def create_book(book: books_schemas.Book, db: DB_SESSION):
    return books_crud.create_book(db, book=book)


@router.get("/{book_id}", response_model=books_schemas.Book)
def get_book(db: DB_SESSION, book_id: int = 1):
    book = books_crud.get_book(db, book_id=book_id)
    return book


@router.put("/{book_id}", response_model=books_schemas.Book)
def update_book(book_id: int, book: books_schemas.Book, db: DB_SESSION):
    return books_crud.update_book(db, book_id=book_id, book=book)


@router.delete("/{book_id}", status_code=204)
def delete_book(book_id: int, db: DB_SESSION):
    if books_crud.delete_book(db, book_id=book_id):
        return {"detail": "Book deleted"}
    raise HTTPException(status_code=404, detail="Not found")
