# from cerberus import Validator
from user.model import UserRole
from setting import db
import bson


users = db['users']


# users.create_index('username', unique=True)


def insert_user(username, password):
    new_user = {"username": username, "password": password,
                "role": UserRole.REGULAR.value}

    inserted_user = users.insert_one(new_user)

    print("*"*20)
    print(get_by_id(bson.ObjectId("6482cced92ae4051c7580681")))
    # return inserted_user


def delete_user(username):
    users.delete_one({"username": username})


def update_user(username, password):
    condition = {"username": username}
    newvalues = {"$set": {"password": password}}

    user = users.update_one(condition, newvalues)
    return user


def get_users():
    docs = users.find()
    return docs


def get_by_username(username):
    return users.find_one({"username": username})


def get_by_id(id):
    return users.find_one({"_id": id})

# # make super admin
# user = {"username": "admin",
#         "password": "123"}

# users.insert_one(**user)
