from sqlalchemy import Column, Integer, Boolean, String

from sql_app.database import Base


class BookDB(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(20))
    title = Column(String(30), nullable=True)
    author = Column(String(30))
    description = Column(String(512), nullable=True)
    price = Column(Integer)

    def __str__(self):
        return f"{self.name} ({self.author})"

    def __repr__(self):
        return f"{self.name} ({self.author})"
