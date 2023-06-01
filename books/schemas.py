from pydantic import BaseModel


class Book(BaseModel):
    """ Pydantic model for request """

    id: int | None = None
    name: str
    title: str | None = None
    author: str
    description: str | None = None
    price: int

    class Config:
        orm_mode = True
