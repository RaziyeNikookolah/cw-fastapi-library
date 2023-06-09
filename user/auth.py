from datetime import datetime, timedelta
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jose import jwt
from user.crud import users
from user.model import UserInDB, UserRequest, UserDisplay, UserRole
from setting import setting
from user.crud import get_by_username

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

ACCESS_TOKEN_EXPIRE_MINUTES = 30
SECRET_KEY = setting.jwt_secret_key
ALGORITHM = setting.jwt_algorythm


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    print(token)
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        username: str = payload.get("sub")
        print(username)
        if username is None:
            raise credentials_exception

    except:
        raise credentials_exception
    user = UserInDB(**get_by_username(username))
    if user is None:
        raise credentials_exception
    return user


def encode_access_token(data: dict):
    SECRET_KEY = "YOUR-SECRET-KEY"
    ALGORITHM = "HS256"
    expire = datetime.utcnow() + timedelta(minutes=60)
    data.update({"expire_date": datetime.strftime(expire, "%Y %m %d")})
    encoded_token = jwt.encode(data, str(SECRET_KEY), algorithm=ALGORITHM)
    return encoded_token


def decode_access_token(token: str):
    SECRET_KEY = "YOUR-SECRET-KEY"
    ALGORITHM = "HS256"
    try:
        decoded_token = jwt.decode(token, str(SECRET_KEY), ALGORITHM)
        username = decoded_token.get("sub")
    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    else:
        return username


def check_admin(user: Annotated[UserInDB, Depends(get_current_user)]):
    if not user.isAdmin:
        raise credentials_exception
    return user
