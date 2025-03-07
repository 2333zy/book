from abc import ABC, abstractmethod


class BookDeleteService(ABC):
    @abstractmethod
    def delete_book(self,book_id: int):
        pass