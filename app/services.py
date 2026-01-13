from app.models import Product
from app.repository import accessJson


default_products = accessJson()


def get_products_service(): #from service.py
    return default_products


def update_product_service(product_id: int, product: Product):
    has_product = False
    product_index = -1
    for i, p in enumerate(default_products):
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
    default_products[product_index] = updated_product
    # Save: file/database
    # call model to save the product

    return updated_product
