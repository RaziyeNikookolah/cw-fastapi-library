# from cerberus import Validator
from setting import db
from bson.objectid import ObjectId
from book.model import BookAvailability, SearchItem,BookRequest

books = db['books']


# books.create_index('title', unique=True)


def insert_book(book_request:BookRequest):
    inserted_book_id = books.insert_one(book_request.dict()).inserted_id
    book = get_by_id(inserted_book_id)
    return book


def delete_book(title):
    books.delete_one({"title": title})


def update_book(title, availability_status):
    condition = {"title": title}
    newvalues = {"$set": {"availability_status": availability_status}}

    books.update_one(condition, newvalues)


def get_books():
    docs = list(books.find())
    for book in docs:
        book["_id"] = str(book["_id"])
    return docs


def get_by_id(id: str):
    book = books.find_one({"_id": ObjectId(id)})
    book["_id"] = str(book["_id"])
    return book


def get_by_title(title):
    return books.find({"title": title})


def search(type: SearchItem, input: str):
    docs=list(books.find({f'{type}': input}))
    for book in docs:
        book["_id"] = str(book["_id"])
    return docs
