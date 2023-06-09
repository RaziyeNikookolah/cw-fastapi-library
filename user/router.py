from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from user.model import UserInDB, UserRequest, UserDisplay
from datetime import timedelta
from user.crud import users
from user.auth import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from typing import Annotated, Any
from user.auth import get_current_user


router = APIRouter(prefix="/users", tags=["user"])


@router.get("/")
def get_me(user: UserInDB = Depends(get_current_user)):
    return user


@router.get("/get_users")
def get_all_users():
    return list(users.values())


@router.post("/login")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    username = form_data.username
    password = form_data.password
    user_dict = users.get(username)

    if not user_dict:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect Username")
    if user_dict.get("password") != password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Password Incorrect")
    user = UserInDB(**user_dict)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=UserDisplay, summary="Regiser user")
def create_user(user: UserRequest) -> Any:
    if user.username in users:
        raise HTTPException(status.HTTP_400_BAD_REQUEST)
    # user.password = get_password_hash(user.password)
    user = UserInDB(**user.dict())
    users[user.username] = user
    return user


@router.delete("/delete", status_code=status.HTTP_201_CREATED, response_model=UserDisplay, summary="Deleting user")
def delete_user(username: str) -> Any:
    if username in users:
        raise HTTPException(status.HTTP_400_BAD_REQUEST)
    # user.password = get_password_hash(user.password)
    user = UserInDB(**user.dict())
    users.pop(username)


@router.put("/update", status_code=status.HTTP_201_CREATED, response_model=UserDisplay, summary="Update user")
def update_user(username: str, user: UserRequest) -> Any:
    if username in users:
        raise HTTPException(status.HTTP_400_BAD_REQUEST)
    # user.password = get_password_hash(user.password)
    user = UserInDB(**user.dict())
    users[username] = user
    return user
