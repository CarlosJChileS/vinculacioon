from fastapi import FastAPI

from .ia_module.controllers.audio_controller import router as audio_router
from .presentations.controllers.upload_controller import router as presentations_router
from .practices.controllers.session_controller import router as practices_router
from .grading.controllers.grading_controller import router as grading_router

app = FastAPI(title="ExposIA API")

app.include_router(audio_router, prefix="/ia")
try:
    from .ia_module.ia_extras.face_detection.detection import router as face_router
    app.include_router(face_router, prefix="/ia/face-detection")
except ImportError:
    pass

app.include_router(presentations_router, prefix="/presentations")
app.include_router(practices_router, prefix="/practices")
app.include_router(grading_router, prefix="/grading")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
