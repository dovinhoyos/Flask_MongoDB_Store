import os
import uuid
from werkzeug.utils import secure_filename
from flask import (
    Blueprint,
    request,
    jsonify,
    current_app,
    render_template,
    redirect,
    url_for,
)
from app.repositories.product_repository import ProductRepository
from app.services.product_service import ProductService

product_bp = Blueprint("product_bp", __name__)

UPLOAD_FOLDER = "app/static/images"

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}


def save_image(file):
    if not file or file.filename == "":
        return ""
    ext = os.path.splitext(file.filename)[1].lower()

    if ext not in ALLOWED_EXTENSIONS:
        return ""  # O lanzar un error

    filename = f"{uuid.uuid4().hex}{ext}"
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)
    return f"/static/images/{filename}"


# Lazy DI
def get_service():
    repo = ProductRepository(current_app.db)
    return ProductService(repo)


@product_bp.route("/", methods=["GET"])
def get_all():
    service = get_service()
    return jsonify(service.list_products())


@product_bp.route("/<product_id>", methods=["GET"])
def get_one(product_id):
    service = get_service()
    product = service.get_product(product_id)
    return jsonify(product) if product else ("Not Found", 404)


@product_bp.route("/", methods=["POST"])
def create():
    service = get_service()
    data = request.json
    new_id = service.create_product(data)
    return jsonify({"id": new_id}), 201


@product_bp.route("/<product_id>", methods=["PUT"])
def update(product_id):
    service = get_service()
    data = request.json
    service.update_product(product_id, data)
    return ("", 204)


@product_bp.route("/<product_id>", methods=["DELETE"])
def delete(product_id):
    service = get_service()
    service.delete_product(product_id)
    return ("", 204)


@product_bp.route("/web", methods=["GET"])
def products_page():
    service = get_service()
    products = service.list_products()
    return render_template("products/list.html", products=products)


@product_bp.route("/web/create", methods=["GET", "POST"])
def create_product_form():
    service = get_service()
    if request.method == "POST":
        image_file = request.files.get("image_file")
        image_url = save_image(image_file)

        data = {
            "code": request.form["code"],
            "name": request.form["name"],
            "price": float(request.form["price"]),
            "category": request.form["category"],
            "image_url": image_url,
        }

        service.create_product(data)
        return redirect(url_for("product_bp.products_page"))

    return render_template("products/form.html")


@product_bp.route("/web/edit/<product_id>", methods=["GET", "POST"])
def edit_product_form(product_id):
    service = get_service()

    if request.method == "POST":
        image_file = request.files.get("image_file")
        image_url = save_image(image_file)

        data = {
            "code": request.form["code"],
            "name": request.form["name"],
            "price": float(request.form["price"]),
            "category": request.form["category"],
            "image_url": request.form["image_url"],
        }

        if image_url:
            data["image_url"] = image_url

        service.update_product(product_id, data)
        return redirect(url_for("product_bp.products_page"))

    product = service.get_product(product_id)
    if not product:
        return "Producto no encontrado", 404
    return render_template("products/form.html", product=product)


@product_bp.route("/web/delete/<product_id>", methods=["POST"])
def delete_product(product_id):
    service = get_service()
    service.delete_product(product_id)
    return redirect(url_for("product_bp.products_page"))
