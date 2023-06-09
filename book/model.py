from pydantic import BaseModel
from enum import Enum


class BookAvailability(str, Enum):
    AVAILABLE = "available"
    NOT_AVAILABLE = "Not available"


class BookRequest(BaseModel):
    title: str
    author: str
    publication_year: int
    genre: str


class BookInDB(BookRequest):
    availability_status: BookAvailability


class BookDisplay(BaseModel):
    title: str
    author: str
    genre: str
