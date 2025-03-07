from datetime import datetime

from application.domain_service.book_delete_service import BookDeleteService
from domain.repository.book_repository import BookRepository
from domain.repository.unit_of_work import UnitOfWork


class BookDeleteServiceImpl(BookDeleteService):
    def __init__(self, uow: UnitOfWork, repository: BookRepository):
        self.uow = uow
        self.repository = repository

    def delete_book(self, book_id: int):
        try:
            self.repository.delete(book_id)
            self.uow.commit()
        except Exception:
            self.uow.rollback()
            raise