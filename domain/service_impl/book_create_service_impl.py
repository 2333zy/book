from datetime import datetime

from application.domain_service.book_create_service import BookCreateService
from domain.entity.book import Book
from domain.repository.book_repository import BookRepository
from domain.repository.unit_of_work import UnitOfWork


class BookCreateServiceImpl(BookCreateService):
    def __init__(self, uow: UnitOfWork, repository: BookRepository):
        self.uow = uow
        self.repository = repository

    def create_book(self, name: str, author: str, date: datetime) -> Book:
        try:
            book_orm = self.repository.create(name, author, date)
            self.uow.commit()
            return book_orm.to_entity()
        except Exception:
            self.uow.rollback()
            raise