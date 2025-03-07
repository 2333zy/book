from abc import ABC, abstractmethod
from datetime import datetime

from domain.entity.book import Book


class BookCommandService(ABC):
    @abstractmethod
    def create_book(self, name: str, author: str, date: datetime) ->Book:
        pass

    @abstractmethod
    def delete_book(self, book_id: int):
        pass

    @abstractmethod
    def update_book(self, book_id: int, name: str, author: str, date: datetime):
        pass