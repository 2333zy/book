from abc import ABC, abstractmethod
from typing import Optional

from domain.entity.book import Book


class BookQueryService(ABC):
    @abstractmethod
    def get_book_by_id(self,book_id: int) -> Optional[Book]:
        pass