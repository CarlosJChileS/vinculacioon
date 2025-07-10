from .upload_controller import router as upload_router
from .user_controller import router as user_router
from .topic_controller import router as topic_router
from .presentation_controller import router as presentation_router
from .slide_controller import router as slide_router

__all__ = [
    "upload_router",
    "user_router",
    "topic_router",
    "presentation_router",
    "slide_router",
]
