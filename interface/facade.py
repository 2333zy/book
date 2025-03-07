import traceback
from http.client import HTTPException
from venv import logger

from fastapi import FastAPI, Depends, status, HTTPException

from application.model.book_create_model import BookCreateModel
from application.model.book_query_model import BookQueryModel
from application.service_impl.book_command_service_impl import BookCommandServiceImpl
from domain.service_impl.book_create_service_impl import BookCreateServiceImpl
from domain.service_impl.book_delete_service_impl import BookDeleteServiceImpl
from domain.service_impl.book_update_service_impl import BookUpdateServiceImpl
from infrastructure.db.database import get_session
from infrastructure.db.repository.book_repository_impl import BookRepositoryImpl
from infrastructure.db.unit_of_work_impl import UnitOfWorkImpl
from interface.app_service.book_command_service import BookCommandService

app = FastAPI()


def book_command_service() -> BookCommandService:
    with get_session() as session:
        uow = UnitOfWorkImpl(session)
        repository = BookRepositoryImpl(session)
        create_service = BookCreateServiceImpl(uow, repository)
        delete_service = BookDeleteServiceImpl(uow, repository)
        update_service = BookUpdateServiceImpl(uow, repository)
        return BookCommandServiceImpl(create_service, delete_service, update_service)


@app.post('/book')
async def create_book(data: BookCreateModel, command_service: BookCommandService = Depends(book_command_service)):
    try:
        print(data)
        new_book = command_service.create_book(data.name, data.author, data.date)
        return BookQueryModel.from_entity(new_book)

    except Exception as err:
        print(traceback.format_exc())
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))


@app.delete('/book/{book_id}')
async def delete_book(book_id: int, command_service: BookCommandService = Depends(book_command_service)):
    try:
        print(book_id)
        command_service.delete_book(book_id)

    except Exception as err:
        print(traceback.format_exc())
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))


@app.put('/book/{book_id}')
async def update_book(book_id: int, data: BookQueryModel, command_service: BookCommandService = Depends(book_command_service)):
    try:
        print(data)
        command_service.update_book(book_id, data.name, data.author, data.date)
    except Exception as err:
        print(traceback.format_exc())
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))
