from fastapi import APIRouter, status, HTTPException, Depends
from typing import List
from book.model import BookAvailability, BookInDB, BookRequest, BookDisplay
from user.auth import get_current_user, check_admin

router = APIRouter(prefix="/books", tags=["Post"])


books = dict()


@router.get(
    "/", response_model=List[BookDisplay], dependencies=[Depends(get_current_user)]
)
def get_books():
    return list(books.values())


@router.post(
    "/", status_code=status.HTTP_201_CREATED, dependencies=[Depends(get_current_user)]
)
def create_book(book: BookRequest):

    if book.title in books:
        raise HTTPException(status.HTTP_400_BAD_REQUEST)

    books[book.title] = book
    return book


@router.get(
    "/{title}", response_model=BookInDB, dependencies=[Depends(get_current_user)]
)
def get_book(title: str):

    book = books.get(title)

    if not book:

        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return book


@router.put("/{title}", dependencies=[Depends(check_admin)])
def update_post(title: str, book_new):

    book_pr = books.get(title)

    if not book_pr:

        raise HTTPException(status.HTTP_404_NOT_FOUND)

    books[book_new.title] = book_new

    return book_new


@router.delete("/{title}", dependencies=[Depends(check_admin)])
def delete_book(title: str):
    book = books.get(title)
    if not book:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    books.pop(title)
    return {"message": "book deleted"}
