from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from sql_app.database import Base


class BookDB(Base):
    __tablename__ = "book"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String(20))
    title: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    author: Mapped[str] = mapped_column(String(30))
    description: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    price: Mapped[int]

    def __str__(self):
        return f"{self.name} ({self.author})"

    def __repr__(self):
        return f"{self.name} ({self.author})"
