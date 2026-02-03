# get list of users
from fastapi import APIRouter, Response
from app.models.models import Username
from app.services.username_service import (
    get_usernames_service
)
from app.utils import standardize_response

router = APIRouter(prefix="/usernames")


@router.get("/")
async def get_usernames():
    usernames = get_usernames_service()
    return standardize_response(usernames, "usernames fetched successfully")
