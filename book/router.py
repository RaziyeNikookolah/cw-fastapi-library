from fastapi import APIRouter, status, HTTPException, Depends
from typing import List
from book.model import BookAvailability, BookInDB, BookRequest, BookDisplay
from user.auth import get_current_user, check_admin
from book.crud import get_by_id, get_books, insert_book


router = APIRouter(prefix="/books", tags=["Book"])



@router.get(
    "/"
)
def get_all_books():
    books = get_books()
    return books


@router.post(
    "/", status_code=status.HTTP_201_CREATED
)
def create_book(book: BookRequest):
    inserted_book = insert_book(**book.dict())
    return inserted_book
    


@router.get(
    "/{book_id}", response_model=BookDisplay
)
def get_book(id: str):
    book = BookInDB(**get_by_id(id))
    if not book:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return book


# @router.put("/{title}", dependencies=[Depends(check_admin)])
# def update_post(title: str, book_new):

#     book_pr = books.get(title)

#     if not book_pr:

#         raise HTTPException(status.HTTP_404_NOT_FOUND)

#     books[book_new.title] = book_new

#     return book_new


# @router.delete("/{title}", dependencies=[Depends(check_admin)])
# def delete_book(title: str):
#     book = books.get(title)
#     if not book:
#         raise HTTPException(status.HTTP_404_NOT_FOUND)
#     books.pop(title)
#     return {"message": "book deleted"}
