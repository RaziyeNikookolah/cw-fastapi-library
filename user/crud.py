from cerberus import Validator
from user.model import UserRole
from setting import db


users = db['users']


users.create_index('username', unique=True)


def insert_user(username, password):
    new_user = {"username": username, "password": password,
                "role": UserRole.REGULAR.value}

    inserted_id = users.insert_one(new_user)


def delete_user(username):
    users.delete_one({"username": username})


def update_user(username, password):
    condition = {"username": username}
    newvalues = {"$set": {"password": password}}

    users.update_one(condition, newvalues)


def display_user():
    docs = users.findall()
    return docs


def display_by_username(username):
    return users.find({"username": username})


# make super admin
user = {"username": "raziye",
        "password": "123", "role": UserRole.ADMIN.value}

users.insert_one(user)
