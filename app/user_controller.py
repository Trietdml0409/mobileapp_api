from fastapi import APIRouter, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json



from app.models import Product
from app.utils import standardize_response
from app.services import get_products_service, update_product_service




router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello world"}

@router.get("/products")
async def get_products():
    products = get_products_service()
    return standardize_response(products, "Products fetched successfully")

@router.put("/products/{product_id}")
async def update_product(product_id: int, product: Product):
    updated_product = update_product_service(product_id, product)
    if not updated_product:
        return Response(status_code=404, content="Product not found")

    return standardize_response(
        updated_product, custom_message="Product updated successfully"
    )
