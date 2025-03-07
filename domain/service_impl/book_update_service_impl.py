from datetime import datetime

from application.domain_service.book_update_service import BookUpdateService
from domain.repository.book_repository import BookRepository
from domain.repository.unit_of_work import UnitOfWork


class BookUpdateServiceImpl(BookUpdateService):
    def __init__(self, uow: UnitOfWork, repository: BookRepository):
        self.uow = uow
        self.repository = repository

    def update_book(self, book_id: int, name: str, author: str, date: datetime):
        try:
            book=self.repository.find_book_by_id(book_id)
            if book is None:
                raise Exception(f'未找到对应的{book_id}')
            book.author = author
            book.name = name
            book.date = date
            self.repository.update(book)
            self.uow.commit()
        except Exception:
            self.uow.rollback()
            raise