from fastapi import FastAPI

from .ia_module.controllers import audio_router, metric_router, feedback_router
from .presentations.controllers import (
    upload_router, user_router, topic_router, presentation_router, slide_router
)
from .practices.controllers import (
    recording_router,
    fragment_router,
    navigation_router,
    public_router,
    practice_router,
    session_router,
)
from .grading.controllers import (
    grading_router,
    grade_router,
    detail_router,
    criterion_router,
    grade_feedback_router,
    external_router,
)

app = FastAPI(title="ExposIA API")

app.include_router(audio_router, prefix="/ia")
app.include_router(metric_router, prefix="/ia")
app.include_router(feedback_router, prefix="/ia")
try:
    from .ia_module.ia_extras.face_detection.detection import router as face_router
    app.include_router(face_router, prefix="/ia/face-detection")
except ImportError:
    pass

app.include_router(upload_router, prefix="/presentations")
app.include_router(user_router, prefix="/presentations")
app.include_router(topic_router, prefix="/presentations")
app.include_router(presentation_router, prefix="/presentations")
app.include_router(slide_router, prefix="/presentations")
for r in [recording_router, fragment_router, navigation_router, public_router, practice_router, session_router]:
    app.include_router(r, prefix="/practices")
for r in [grading_router, grade_router, detail_router, criterion_router, grade_feedback_router, external_router]:
    app.include_router(r, prefix="/grading")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
