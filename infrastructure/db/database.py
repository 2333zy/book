from contextlib import contextmanager
from datetime import datetime
from typing import Iterator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from domain.entity.book import Book
from infrastructure.db.model.base import Base

# noinspection PyUnresolvedReferences
from infrastructure.db.model.book_model import BookModel
from infrastructure.db.repository.book_repository_impl import BookRepositoryImpl

from settings.develop import WFS_DB_URL

engine = create_engine(WFS_DB_URL)
Base.metadata.create_all(engine)


@contextmanager
def get_session() -> Iterator[Session]:
    session: Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)()
    try:
        yield session
    finally:
        session.close()

if __name__ == '__main__':
    with get_session() as session:
        book_repository = BookRepositoryImpl(session)
        # book_orm = book_repository.create('数学', 'zzz', datetime.now())
        # session.commit()
        # book = book_orm.to_entity()
        # print(book)
        # book=book_repository.find_book_by_id(2)
        # book.name='yyy'
        # book_repository.update(book)
        # session.commit()
        # print(book)
        book_repository.delete(2)
        session.commit()