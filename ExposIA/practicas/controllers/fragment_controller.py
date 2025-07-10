from fastapi import APIRouter
from ..models import AudioFragment
from ..services.fragment_service import add_fragment, get_fragments

router = APIRouter(prefix="/fragments")

@router.post("/", response_model=AudioFragment)
async def create_fragment_route(frag: AudioFragment):
    return add_fragment(frag)

@router.get("/", response_model=list[AudioFragment])
async def list_fragments_route():
    return get_fragments()
