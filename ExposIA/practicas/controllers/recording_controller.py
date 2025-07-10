from fastapi import APIRouter
from ..models import Recording
from ..services.recording_service import add_recording, get_recordings

router = APIRouter(prefix="/recordings")

@router.post("/", response_model=Recording)
async def create_recording_route(rec: Recording):
    return add_recording(rec)

@router.get("/", response_model=list[Recording])
async def list_recordings_route():
    return get_recordings()
