from app.models.models import Username
from app.repositories.username_repository import load_default_usernames

DEFAULT_USERNAME = load_default_usernames()


def get_usernames_service():  # from service.py
    return DEFAULT_USERNAME