from fastapi import APIRouter
from ..models import PracticeSession
from ..services.session_service import add_session, get_sessions

router = APIRouter(prefix="/sessions")

@router.post("/", response_model=PracticeSession)
async def create_session_route(sess: PracticeSession):
    return add_session(sess)

@router.get("/", response_model=list[PracticeSession])
async def list_sessions_route():
    return get_sessions()
