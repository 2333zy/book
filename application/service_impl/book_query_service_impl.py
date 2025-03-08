from typing import Optional, List

from domain.entity.book import Book
from domain.repository.book_repository import BookRepository
from interface.app_service.book_query_service import BookQueryService


class BookQueryServiceImpl(BookQueryService):
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def get_book_by_id(self, book_id: int) -> Optional[Book]:
        return self.repository.find_book_by_id(book_id)

    def get_all_books(self) -> List[Book]:
        return self.repository.get_all_books()