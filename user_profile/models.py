from sqlalchemy.orm import Mapped, mapped_column

from sql_app.database import Base


class UserProfileDB(Base):
    __tablename__ = "user_profile"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    column_name: Mapped[bool] = mapped_column(default=True)
    column_title: Mapped[bool] = mapped_column(default=True)
    column_author: Mapped[bool] = mapped_column(default=True)
    column_description: Mapped[bool] = mapped_column(default=True)
    column_price: Mapped[bool] = mapped_column(default=True)
