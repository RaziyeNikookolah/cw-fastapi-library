from pydantic import BaseModel
from enum import Enum


class UserRole(str, Enum):
    REGULAR = "regular"
    ADMIN = "admin"


class UserRequest(BaseModel):
    username: str
    password: str


class UserInDB(UserRequest):
    role: UserRole


class UserDisplay(BaseModel):
    _id: str
    username: str
    role: UserRole
