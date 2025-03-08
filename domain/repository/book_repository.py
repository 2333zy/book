from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional, List

from domain.entity.book import Book
from infrastructure.db.model.book_model import BookModel


class BookRepository(ABC):
    @abstractmethod
    def create(self, name: str, author: str, date: datetime) -> BookModel:
        pass

    @abstractmethod
    def delete(self, book_id: int) -> None:
        pass

    @abstractmethod
    def update(self, book: Book) -> None:
        pass

    @abstractmethod
    def find_book_by_id(self, book_id: int) -> Optional[Book]:
        pass

    @abstractmethod
    def get_all_books(self) -> List[Book]:
        pass
