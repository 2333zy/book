from sqlalchemy.orm import Session

from domain.repository.unit_of_work import UnitOfWork


class UnitOfWorkImpl(UnitOfWork):
    def __init__(self, session: Session):
        self.session = session

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()