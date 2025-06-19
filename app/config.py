import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret")
    MONGO_URI = os.getenv("MONGO_URI")
    MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "app/static/images")

    @staticmethod
    def init_app(app):
        if not Config.MONGO_URI or not Config.MONGO_DB_NAME:
            print("⚠️  Advertencia: Configuración de Mongo incompleta.")

class TestingConfig(Config):
    TESTING = True
    MONGO_DB_NAME = "testing_db"

class ProductionConfig(Config):
    DEBUG = False
