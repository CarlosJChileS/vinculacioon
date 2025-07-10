from fastapi import APIRouter
from ..models import SesionPractica
from ..services.session_service import add_session, get_sessions

router = APIRouter(prefix="/sesiones")

@router.post("/", response_model=SesionPractica)
async def create_session_route(sess: SesionPractica):
    return add_session(sess)

@router.get("/", response_model=list[SesionPractica])
async def list_sessions_route():
    return get_sessions()
