from fastapi import APIRouter, UploadFile, File
from ..dtos.analysis_dto import AudioAnalysisInput, AnalysisResult
from ..services.audio_service import process_audio
from ..mappers.audio_mapper import to_dto

router = APIRouter()

@router.post("/analisis", response_model=AnalysisResult)
async def analizar_archivo(audio: UploadFile = File(...)):
    """Analiza un archivo de audio y devuelve las metricas principales."""
    data = AudioAnalysisInput(filename=audio.filename, content=await audio.read())
    result = process_audio(data)
    return to_dto(result)
