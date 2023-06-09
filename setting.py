from dotenv import load_dotenv
from pathlib import Path
from pymongo import MongoClient
from os import getenv


env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


client = MongoClient("mongodb://localhost:27017/")
db = client['library']


class Setting:
    jwt_secret_key: str = getenv("SECRET_KEY")
    jwt_algorythm: str = getenv("ALGORITHM")
    # admin_pass: str = getenv("ADMIN_PASS")


setting = Setting()
