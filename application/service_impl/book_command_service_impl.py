from datetime import datetime

from application.domain_service.book_create_service import BookCreateService
from application.domain_service.book_delete_service import BookDeleteService
from application.domain_service.book_update_service import BookUpdateService
from domain.entity.book import Book
from interface.app_service.book_command_service import BookCommandService


class BookCommandServiceImpl(BookCommandService):
    def __init__(self, create_service: BookCreateService, delete_service: BookDeleteService, update_service:BookUpdateService):
        self.create_service = create_service
        self.delete_service = delete_service
        self.update_service = update_service

    def create_book(self, name: str, author: str, date: datetime) ->Book:
        return self.create_service.create_book(name, author, date)

    def delete_book(self, book_id: int):
        self.delete_service.delete_book(book_id)

    def update_book(self, book_id: int, name: str, author: str, date: datetime):
        self.update_service.update_book(book_id, name, author, date)