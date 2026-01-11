from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json

from models import Product
from utils import standardize_response
from services import get_products_service, update_product_service

app = FastAPI()

# Define the origins that are allowed to make requests
origins = [
    "http://localhost:3000",  # Example: your React or Vue frontend development server
    # "https://www.your-frontend-domain.com",  # Example: your production frontend domain
    # You can add more origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,  # Allow cookies to be sent with requests
    allow_methods=["*"],  # Allow all standard methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)


@app.get("/")
async def root():
    return {"message":"Hello world"}


# Getting the current user, this is the fixed path
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


# Return an Id with {user_id} passed in
@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/products")
async def get_products():
    products = get_products_service()

    return standardize_response(products, "Products fetched successfully")


# Update a product by id
@app.put("/products/{product_id}")
async def update_product(product_id: int, product: Product):
    updated_product = update_product_service(product_id, product)
    if not updated_product:
        return Response(status_code=404, content="Product not found")

    return standardize_response(
        updated_product, custom_message="Product updated successfully"
    )
