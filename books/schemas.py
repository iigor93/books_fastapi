from pydantic import BaseModel, Field


class Book(BaseModel):
    """ Pydantic model for request """

    id: int | None = None
    name: str
    title: str | None = None
    author: str
    description: str | None = None
    price: int = Field(gt=0, le=99999)

    class Config:
        orm_mode = True
