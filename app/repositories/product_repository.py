from bson.objectid import ObjectId


class ProductRepository:
    def __init__(self, db):
        self.collection = db.products

    def get_all(self):
        return list(self.collection.find())

    def get_by_id(self, product_id):
        return self.collection.find_one({"_id": ObjectId(product_id)})

    def create(self, data):
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

    def update(self, product_id, data):
        self.collection.update_one({"_id": ObjectId(product_id)}, {"$set": data})

    def delete(self, product_id):
        self.collection.delete_one({"_id": ObjectId(product_id)})
