from datetime import datetime

from pydantic import BaseModel, Field

from domain.entity.book import Book


class BookQueryModel(BaseModel):
    name: str
    author: str
    date: datetime

    @staticmethod
    def from_entity(book:Book) ->'BookQueryModel':
        return BookQueryModel(name=book.name, author=book.author, date=book.date)