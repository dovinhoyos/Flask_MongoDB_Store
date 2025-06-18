from flask import (
    Blueprint,
    request,
    render_template,
    redirect,
    url_for,
    session,
    current_app,
)
from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService

auth_bp = Blueprint("auth_bp", __name__)


def get_service():
    repo = UserRepository(current_app.db)
    return AuthService(repo)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    service = get_service()
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = service.authenticate(email, password)
        if not user:
            return render_template("auth/login.html", error="Credenciales inválidas")

        session["user_id"] = user["id"]
        session["role"] = user["role"]
        session["email"] = user["email"]

        return redirect(url_for("product_bp.products_page"))

    return render_template("auth/login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth_bp.login"))


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    service = get_service()
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        confirm = request.form.get("confirm")

        if password != confirm:
            return render_template(
                "auth/register.html", error="Las contraseñas no coinciden"
            )

        if service.repo.find_by_email(email):
            return render_template(
                "auth/register.html", error="El email ya está registrado"
            )

        # 1. Registramos
        service.register(email, password)

        # 2. Obtenemos el user
        user = service.repo.find_by_email(email)

        # 3. Logueamos en sesión
        session["user_id"] = str(user["_id"])
        session["role"] = user.get("role", "user")
        session["email"] = user["email"]

        return redirect(url_for("product_bp.products_page"))

    return render_template("auth/register.html")
