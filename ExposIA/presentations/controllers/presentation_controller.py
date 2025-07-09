from fastapi import APIRouter
from ..models import Presentation
from ..services.presentation_service import add_presentation, get_presentations

router = APIRouter(prefix="/presentations")

@router.post("/", response_model=Presentation)
async def create_presentation_route(pres: Presentation):
    return add_presentation(pres)

@router.get("/", response_model=list[Presentation])
async def list_presentations_route():
    return get_presentations()
