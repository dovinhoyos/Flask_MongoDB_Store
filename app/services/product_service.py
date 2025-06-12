from app.models.product_model import product_schema


class ProductService:
    def __init__(self, repository):
        self.repository = repository

    def list_products(self):
        return [product_schema(p) for p in self.repository.get_all()]

    def get_product(self, product_id):
        prod = self.repository.get_by_id(product_id)
        return product_schema(prod) if prod else None

    def create_product(self, data):
        return self.repository.create(data)

    def update_product(self, product_id, data):
        self.repository.update(product_id, data)

    def delete_product(self, product_id):
        self.repository.delete(product_id)
