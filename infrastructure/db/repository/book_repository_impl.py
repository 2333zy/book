from datetime import datetime
from typing import Optional, List

from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from domain.entity.book import Book
from domain.repository.book_repository import BookRepository
from infrastructure.db.model.book_model import BookModel


class BookRepositoryImpl(BookRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, name: str, author: str, date: datetime) -> BookModel:
        book_orm = BookModel(name=name, author=author, date=date)
        self.session.add(book_orm)
        return book_orm

    def delete(self, book_id: int) -> None:
        book_orm = self.session.query(BookModel).filter_by(id=book_id).one()
        self.session.delete(book_orm)

    def update(self, book: Book) -> None:
        book_orm = self.session.query(BookModel).filter_by(id=book.book_id).one()
        book_orm.merge_entity(book)
        self.session.merge(book_orm)

    def find_book_by_id(self, book_id: int) -> Optional[Book]:
        try:
            book_orm = self.session.query(BookModel).filter_by(id=book_id).one()
            return book_orm.to_entity()
        except NoResultFound:
            return None

    def get_all_books(self) -> List[Book]:
        books_orm = self.session.query(BookModel).all()
        return [book_orm.to_entity() for book_orm in books_orm]
