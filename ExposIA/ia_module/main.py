from fastapi import FastAPI
from .controllers.audio_controller import router as audio_router

app = FastAPI(
    title="ExposIA IA Module",
    description="API de analisis de audio para exposiciones orales"
)

app.include_router(audio_router)

try:
    from .ia_extras.face_detection.detection import router as face_router
    app.include_router(face_router, prefix="/face-detection")
except ImportError:
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
