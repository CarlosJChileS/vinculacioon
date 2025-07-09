from fastapi import APIRouter
from ..models import Slide, SlideNote
from ..services.slide_service import add_slide, get_slides, add_note, get_notes

router = APIRouter(prefix="/slides")

@router.post("/", response_model=Slide)
async def create_slide_route(slide: Slide):
    return add_slide(slide)

@router.get("/", response_model=list[Slide])
async def list_slides_route():
    return get_slides()

@router.post("/notes", response_model=SlideNote)
async def create_note_route(note: SlideNote):
    return add_note(note)

@router.get("/notes", response_model=list[SlideNote])
async def list_notes_route():
    return get_notes()
