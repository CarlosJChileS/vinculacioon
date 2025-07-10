from fastapi import APIRouter
from ..models import User
from ..services.user_service import add_user, get_users

router = APIRouter(prefix="/users")

@router.post("/", response_model=User)
async def create_user_route(user: User):
    return add_user(user)

@router.get("/", response_model=list[User])
async def list_users_route():
    return get_users()
