from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from user_controller import router  # import your controller
import json



from app.models import Product
from app.utils import standardize_response
from app.services import get_products_service, update_product_service

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

