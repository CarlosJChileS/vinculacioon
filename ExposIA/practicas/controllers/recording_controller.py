from fastapi import APIRouter, UploadFile, File
from ..models import Recording
from ..services.recording_service import add_recording, get_recordings, add_recording_file

router = APIRouter(prefix="/recordings")

@router.post("/", response_model=Recording)
async def create_recording_route(rec: Recording):
    return add_recording(rec)


@router.post("/upload", response_model=Recording)
async def upload_recording_route(usuario_id: int, presentacion_id: int, audio: UploadFile = File(...)):
    return add_recording_file(usuario_id, presentacion_id, audio)

@router.get("/", response_model=list[Recording])
async def list_recordings_route():
    return get_recordings()
