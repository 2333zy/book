from datetime import datetime

from pydantic import BaseModel, Field


class BookCreateModel(BaseModel):
    name: str = ''
    author: str = ''
    date: datetime = Field(default_factory=datetime.now)