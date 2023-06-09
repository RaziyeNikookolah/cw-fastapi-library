from cerberus import Validator
from setting import db


books = db['books']


books.create_index('title', unique=True)


def insert_book(title, author, publication_year, genre, availability_status):
    new_book = {"title": title, "author": author,
                "publication_year": publication_year, "genre": genre, "availability_status": availability_status}

    return books.insert_one(new_book)


def delete_book(title):
    books.delete_one({"title": title})


def update_book(title, availability_status):
    condition = {"title": title}
    newvalues = {"$set": {"availability_status": availability_status}}

    books.update_one(condition, newvalues)


def display_books():
    docs = books.findall()
    return docs


def display_by_title(title):
    return books.find({"title": title})
