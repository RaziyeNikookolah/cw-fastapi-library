
from passlib.context import CryptContext
mycontext = CryptContext(schemes=["sha256_crypt", "md5_crypt"])


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return mycontext.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return mycontext.hash(password)
