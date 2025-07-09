"""Submodulo opcional de deteccion de emociones faciales."""
from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel

router = APIRouter()

class FaceResult(BaseModel):
    emocion: str
    confianza: float

@router.post("/analizar", response_model=FaceResult)
async def analizar_video(video: UploadFile = File(...)):
    """Analiza un video y devuelve la emocion principal (simulada)."""
    return FaceResult(emocion="felicidad", confianza=0.8)
