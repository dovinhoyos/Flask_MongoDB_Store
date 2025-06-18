from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user_model import user_schema


class AuthService:
    def __init__(self, repo):
        self.repo = repo

    def authenticate(self, email, password):
        user = self.repo.find_by_email(email)
        if not user:
            return None
        if not check_password_hash(user["password"], password):
            return None
        return user_schema(user)

    def register(self, email, password, role="user"):
        hashed = generate_password_hash(password)
        return self.repo.create_user({"email": email, "password": hashed, "role": role})
