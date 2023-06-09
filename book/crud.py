# from cerberus import Validator
from setting import db
from bson.objectid import ObjectId
from book.model import BookAvailability, SearchItem

books = db['books']


# books.create_index('title', unique=True)


def insert_book(title, author, publication_year, genre):
    new_book = {"title": title, "author": author,
                "publication_year": publication_year, "genre": genre, "availability_status": BookAvailability.AVAILABLE.value}
    inserted_book_id = books.insert_one(new_book).inserted_id
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
    print(222222)
    test={f"'{type}'": input}
    print(test)
    return books.find(test)
