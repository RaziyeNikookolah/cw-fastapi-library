from fastapi import APIRouter, status, HTTPException, Depends
from typing import List
from user.auth import get_current_user, check_admin

router = APIRouter(prefix="/books", tags=["Post"])


books = dict()


@router.get(
    "/", response_model=List[PostDb], dependencies=[Depends(get_current_user)]
)
def get_books():
    return list(books.values())


@router.post(
    "/", status_code=status.HTTP_201_CREATED, dependencies=[Depends(get_current_user)]
)
def create_post(post: BasePost):

    if post.title in books:
        raise HTTPException(status.HTTP_400_BAD_REQUEST)

    books[post.title] = post
    return post


@router.get(
    "/{title}", response_model=PostDb, dependencies=[Depends(get_current_user)]
)
def get_post(title: str):

    post = books.get(title)

    if not post:

        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return post


@router.put("/{title}", dependencies=[Depends(check_admin)])
def update_post(title: str, post_new):

    post_pr = books.get(title)

    if not post_pr:

        raise HTTPException(status.HTTP_404_NOT_FOUND)

    books[post_new.title] = post_new

    return {"message": "post updated"}


@router.delete("/{title}", dependencies=[Depends(check_admin)])
def delete_post(title: str):
    post = books.get(title)
    if not post:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    books.pop(title)
    return {"message": "post deleted"}
