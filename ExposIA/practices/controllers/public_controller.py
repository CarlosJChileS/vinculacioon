from fastapi import APIRouter
from ..models import PublicSpeakingSession
from ..services.public_speaking_service import add_public, get_public_sessions

router = APIRouter(prefix="/public")

@router.post("/", response_model=PublicSpeakingSession)
async def create_public_route(ps: PublicSpeakingSession):
    return add_public(ps)

@router.get("/", response_model=list[PublicSpeakingSession])
async def list_public_route():
    return get_public_sessions()
