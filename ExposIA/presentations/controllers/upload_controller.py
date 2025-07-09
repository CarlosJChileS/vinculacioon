from fastapi import APIRouter, UploadFile, File
from ..services.upload_service import save_presentation
from ..dtos.presentation_dto import PresentationInfo

router = APIRouter()

@router.post("/upload", response_model=PresentationInfo)
async def upload_presentation(file: UploadFile = File(...)):
    """Sube un PDF de presentacion."""
    return save_presentation(file)
