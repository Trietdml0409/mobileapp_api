import sys
from pathlib import Path

from app.controllers import product_controller
from app.controllers import user_controller

# Add the project root to Python path to allow absolute imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware


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


# Router root: /
router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello world"}


# include product controller here
app.include_router(product_controller.router)
app.include_router(user_controller.router)
