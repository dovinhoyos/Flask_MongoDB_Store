def user_schema(doc):
    return {
        "id": str(doc["_id"]),
        "email": doc["email"],
        "password": doc["password"],  # hashed
        "role": doc.get("role", "user"),
    }
