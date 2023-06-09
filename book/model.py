from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class BookAvailability(str, Enum):
    AVAILABLE = "available"
    NOT_AVAILABLE = "Not available"


class BorrowData(BaseModel):
    borrow_date: datetime
    user_id: str


class Author(BaseModel):
    first_name: str
    last_name: str


class BookRequest(BaseModel):
    title: str
    author: Author
    publication_year: int
    genre: str
    borrowdata: list(BorrowData)


class BookInDB(BookRequest):
    availability_status: BookAvailability
    _id: str


class BookDisplay(BaseModel):
    title: str
    author: str
    genre: str


class SearchItem(str, Enum):
    TITLE = "title"
    AUTHOR = "author"
    GENRE = "genre"


class SearchRequest(BaseModel):
    type: SearchItem
    input:str