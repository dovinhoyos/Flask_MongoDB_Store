from bson.objectid import ObjectId


class UserRepository:
    def __init__(self, db):
        self.collection = db.users

    def find_by_email(self, email):
        return self.collection.find_one({"email": email})

    def find_by_id(self, user_id):
        return self.collection.find_one({"_id": ObjectId(user_id)})

    def create_user(self, data):
        return self.collection.insert_one(data)
