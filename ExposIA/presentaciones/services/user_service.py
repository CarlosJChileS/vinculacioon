from ..models import User
from ..repositories.user_repo import (
    create_user, list_users, get_user, update_user, delete_user
)


def add_user(data: User) -> User:
    return create_user(data)


def get_users():
    return list_users()
