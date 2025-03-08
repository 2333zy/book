from datetime import datetime

from pydantic import BaseModel, Field

from domain.entity.book import Book


class BookQueryModel(BaseModel):
    book_id: int
    name: str
    author: str
    date: datetime

    @staticmethod
    def from_entity(book: Book) -> 'BookQueryModel':
        return BookQueryModel(book_id=book.book_id, name=book.name, author=book.author, date=book.date)
