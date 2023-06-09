from pydantic import BaseModel
from enum import Enum


class UserRole(str, Enum):
    REGULAR = "regular"
    ADMIN = "admin"


class UserRequest(BaseModel):
    username: str
    password: str


class UserInDB(UserRequest):
    role: UserRole = UserRole.REGULAR.value


class UserDisplay(BaseModel):
    username: str
    role: UserRole
