from fastapi import APIRouter, UploadFile, File
from ..services.upload_service import save_presentation

router = APIRouter()

@router.post("/upload")
async def upload_presentation(file: UploadFile = File(...)):
    """Sube un PDF de presentacion."""
    path = save_presentation(file)
    return {"stored_at": path}
