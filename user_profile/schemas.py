from pydantic import BaseModel


class UserProfile(BaseModel):
    """ Pydantic model for request """

    id: int = 1
    column_name: bool
    column_title: bool
    column_author: bool
    column_description: bool
    column_price: bool

    class Config:
        orm_mode = True
