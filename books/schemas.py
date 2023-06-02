from typing import Optional

from pydantic import BaseModel, Field


class Book(BaseModel):
    """ Pydantic model for request """

    id: int | None = None
    name: str = Field(min_length=1, max_length=20)
    title: Optional[str] = Field(None, max_length=30)
    author: str
    description: Optional[str] = Field(None, max_length=512)
    price: int = Field(gt=0, le=99999)

    class Config:
        orm_mode = True
