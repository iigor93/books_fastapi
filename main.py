from fastapi import FastAPI

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
