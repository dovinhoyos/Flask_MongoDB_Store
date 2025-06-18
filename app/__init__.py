from flask import Flask
from app.routes.product_routes import product_bp
from app.config import Config
from pymongo import MongoClient
from app.routes.auth_routes import auth_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Init Mongo
    client = MongoClient(app.config["MONGO_URI"])
    app.db = client[app.config["MONGO_DB_NAME"]]

    # Register Blueprints
    app.register_blueprint(product_bp, url_prefix="/products")

    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app
