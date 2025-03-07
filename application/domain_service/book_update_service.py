from abc import ABC, abstractmethod
from datetime import datetime

from domain.entity.book import Book


class BookUpdateService(ABC):
    @abstractmethod
    def update_book(self, book_id: int, name: str, author: str, date: datetime):
        pass