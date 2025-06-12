import os


class Config:
    MONGO_URI = os.getenv(
        "MONGO_URI",
        "mongodb+srv://richard06:Sopl4m3l4v3l4@cluster0.jt6799u.mongodb.net/",
    )
    MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "store")
