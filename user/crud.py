# from cerberus import Validator
from user.model import UserRole
from setting import db
from bson.objectid import ObjectId


users = db['users']


# users.create_index('username', unique=True)


def insert_user(username, password):
    new_user = {"username": username, "password": password,
                "role": UserRole.REGULAR.value}

    inserted_user_id = users.insert_one(new_user).inserted_id
    user = get_by_id(inserted_user_id)
    return user



def delete_user(username):
    users.delete_one({"username": username})


def update_user(username, password):
    condition = {"username": username}
    newvalues = {"$set": {"password": password}}

    user = users.update_one(condition, newvalues)
    return user


def get_users():
    docs = list(users.find())
    for user in docs:
        user["_id"] = str(user["_id"])
        user.pop("password")
    return docs


def get_by_username(username):
    return users.find_one({"username": username})


def get_by_id(id:ObjectId):
    user = users.find_one({"_id": id})
    user["_id"] = str(user["_id"])
    return user




# # make super admin
# user = {"username": "admin",
#         "password": "123"}

# users.insert_one(**user)
