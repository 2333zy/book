from abc import ABC, abstractmethod
from datetime import datetime

from domain.entity.book import Book


class BookCreateService(ABC):
    @abstractmethod
    def create_book(self,name: str, author: str, date: datetime) -> Book:
        pass