from flask import Flask
from app.routes.product_routes import product_bp
from app.routes.auth_routes import auth_bp
from app.config import Config
from pymongo import MongoClient, errors


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Init Mongo con manejo de errores
    try:
        client = MongoClient(app.config["MONGO_URI"])
        app.db = client[app.config["MONGO_DB_NAME"]]
    except errors.ConnectionFailure:
        print("❌ Error: No se pudo conectar a MongoDB")
        app.db = None

    # Register Blueprints
    app.register_blueprint(product_bp, url_prefix="/products")
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app
