from fastapi import FastAPI
from sqlalchemy import text

from sql_app.database import engine

from user_profile import models as user_profile_models
from user_profile import user_profile_app

from books import models as books_models
from books import books_app


user_profile_models.Base.metadata.create_all(bind=engine)
books_models.Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(books_app.router, prefix="/books",)
app.include_router(user_profile_app.router, prefix="/user_profile",)


@app.get("/test/")
def test():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT id, name, title FROM book WHERE id > :id and name = :name"), {"id": 1, "name": "5 book"})
        for row in result:
            print(f"{row.id} {row}")
    return "OK"
