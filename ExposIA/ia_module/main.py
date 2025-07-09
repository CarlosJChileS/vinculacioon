from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from .ia_core.analysis import analyze_audio

app = FastAPI(title="ExposIA IA Module", description="API de analisis de audio para exposiciones orales")

class AnalysisResult(BaseModel):
    velocidad_palabras: float
    claridad: float
    num_pausas: int
    retroalimentacion: str

@app.post("/analisis", response_model=AnalysisResult)
async def analizar_archivo(audio: UploadFile = File(...)):
    """Analiza un archivo de audio y devuelve las metricas principales."""
    result = analyze_audio(await audio.read())
    return result

try:
    from .ia_extras.face_detection.detection import router as face_router
    app.include_router(face_router, prefix="/face-detection")
except ImportError:
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
