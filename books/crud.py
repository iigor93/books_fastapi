from fastapi import HTTPException
from sqlalchemy.orm import Session

import books.models as models
from books import schemas


def get_books_list(db: Session):
    """ Get books list """

    books_list = db.query(models.BookDB).all()
    return books_list


def create_book(db: Session, book: schemas.Book):
    """ Create book """

    book_db = models.BookDB(**book.dict())
    db.add(book_db)
    db.commit()
    db.refresh(book_db)
    return book_db


def get_book(db: Session, book_id: int):
    """ Get book """
    book_db = db.query(models.BookDB).get(book_id)
    if not book_db:
        raise HTTPException(status_code=404, detail="Book not found")
    return book_db


def update_book(db: Session, book_id: int, book: schemas.Book):
    """ Update book """

    book_db = db.query(models.BookDB).get(book_id)
    if book_db:
        book = book.dict(exclude_unset=True)

        for key, value in book.items():
            setattr(book_db, key, value)

        db.add(book_db)
        db.commit()
        db.refresh(book_db)
        return book_db
    raise HTTPException(status_code=404, detail="Book not found")


def delete_book(db: Session, book_id: int):
    """ Delete book """

    book_db = db.query(models.BookDB).get(book_id)
    if book_db:
        db.delete(book_db)
        db.commit()
        return True
    return False
