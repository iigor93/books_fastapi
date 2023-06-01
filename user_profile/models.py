from sqlalchemy import Column, Integer, Boolean

from sql_app.database import Base


class UserProfileDB(Base):
    __tablename__ = "user_profile"

    id = Column(Integer, primary_key=True, index=True)
    column_name = Column(Boolean, default=True)
    column_title = Column(Boolean, default=True)
    column_author = Column(Boolean, default=True)
    column_description = Column(Boolean, default=True)
    column_price = Column(Boolean, default=True)
