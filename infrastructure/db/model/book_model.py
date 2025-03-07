from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from infrastructure.db.model.base import Base
from domain.entity.book import Book

class BookModel(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    author = Column(String)
    date = Column(DateTime)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def merge_entity(self, book: Book):
        self.name = book.name
        self.author = book.author
        self.date = book.date

    def to_entity(self) ->Book:
        return Book(
            book_id=self.id,
            name=self.name,
            author=self.author,
            date=self.date,
        )