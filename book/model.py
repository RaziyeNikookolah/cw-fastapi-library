from pydantic import BaseModel
from enum import Enum


class BookRequest(BaseModel):
    title: str
    author: str
    publication_year: int
    genre: str


class BookInDB(BookRequest):
    availability_status: True


class BookDisplay(BookRequest):
    ...
