from fastapi import APIRouter, status, HTTPException, Depends, Query
from typing import List, Annotated
from book.model import BookAvailability, BookInDB, BookRequest, BookDisplay, SearchRequest
from user.auth import get_current_user, check_admin
from book.crud import get_by_id, get_books, insert_book, search


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
    inserted_book = insert_book(book)
    return inserted_book
    


@router.get(
    "/{book_id}", response_model=BookDisplay
)
def get_book(id: str):
    book = BookInDB(**get_by_id(id))
    if not book:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return book

@router.post(
    "/search"
)
def search_book(search_item : Annotated[str, Query(...,enum=["title","auther","genre"])] ,input: str):
    print(111111)
    result=search(search_item, input)
    return result



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
