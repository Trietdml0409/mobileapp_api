# get list of product


from fastapi import APIRouter, Response
from app.models.models import Product
from app.services.product_service import (
    get_product_service,
    get_products_service,
    update_product_service,
)
from app.utils import standardize_response

router = APIRouter(prefix="/products")


# /products/
@router.get("/")
async def get_products():
    products = get_products_service()
    return standardize_response(products, "Products fetched successfully")


# /products/{product_id}
@router.put("/{product_id}")
async def update_product(product_id: int, product: Product):
    updated_product = update_product_service(product_id, product)
    if not updated_product:
        return Response(status_code=404, content="Product not found")

    return standardize_response(
        updated_product, custom_message="Product updated successfully"
    )



# /products/{product_id}
@router.get("/{product_id}")
async def get_product(product_id: int):
    product = get_product_service(product_id)
    if not product:
        return Response(status_code=404, content="Product not found")

    return standardize_response(product, "Product fetched successfully")
