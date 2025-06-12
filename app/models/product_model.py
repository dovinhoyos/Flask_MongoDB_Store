def product_schema(doc):
    return {
        "id": str(doc["_id"]),
        "code": doc["code"],
        "name": doc["name"],
        "price": doc["price"],
        "category": doc["category"],
        "image_url": doc.get("image_url", ""),
    }
