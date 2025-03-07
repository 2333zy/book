from datetime import datetime


class Book:
    def __init__(self, book_id: int, name: str, author: str, date: datetime):
        self.book_id = book_id
        self.name = name
        self.author = author
        self.date = date

    def __repr__(self):
        return f'Book(book_id={self.book_id}, name={self.name}, author={self.author}, date={self.date})'