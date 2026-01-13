from app.models.models import Product
from app.repositories.product_repository import load_default_products


DEFAULT_PRODUCTS = load_default_products()


def get_products_service():  # from service.py
    return DEFAULT_PRODUCTS


def update_product_service(product_id: int, product: Product):
    has_product = False
    product_index = -1
    for i, p in enumerate(DEFAULT_PRODUCTS):
        if p["id"] == product_id:
            has_product = True
            product_index = i
            break

    if not has_product:
        return None

    updated_product = {
        "id": product_id,
        "name": product.name,
        "price": product.price,
        "image": product.image,
        "createdAt": product.createdAt,
        "isBestSeller": product.isBestSeller,
        "brandName": product.brandName,
        "liked": product.liked,
    }

    # Update the product in the list by index
    DEFAULT_PRODUCTS[product_index] = updated_product
    # Save: file/database
    # call model to save the product

    return updated_product


def get_product_service(product_id: int) -> Product | None:
    for product in DEFAULT_PRODUCTS:
        if product["id"] == product_id:
            return product

    return None
