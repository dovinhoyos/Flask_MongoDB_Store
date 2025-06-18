import os
from dotenv import load_dotenv

# Cargar el archivo .env
load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret")
    MONGO_URI = os.getenv("MONGO_URI")
    MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "app/static/images")
