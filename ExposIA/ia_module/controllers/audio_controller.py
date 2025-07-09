from fastapi import APIRouter, UploadFile, File, HTTPException
from ..dtos.analysis_dto import AudioAnalysisInput, AnalysisResult
from ..services.audio_service import process_audio, process_recording
from ..mappers.audio_mapper import to_dto

router = APIRouter()

@router.post("/analisis", response_model=AnalysisResult)
async def analizar_archivo(audio: UploadFile = File(...)):
    """Analiza un archivo de audio y devuelve las metricas principales."""
    data = AudioAnalysisInput(filename=audio.filename, content=await audio.read())
    result = process_audio(data)
    return to_dto(result)

@router.post("/analisis/grabaciones/{grabacion_id}", response_model=AnalysisResult)
async def analizar_grabacion(grabacion_id: str):
    """Analiza una grabacion existente por identificador."""
    try:
        result = process_recording(grabacion_id)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Grabacion no encontrada")
    return to_dto(result)
