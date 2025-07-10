from .session_controller import router as session_router
from .recording_controller import router as recording_router
from .fragment_controller import router as fragment_router
from .navigation_controller import router as navigation_router
from .public_controller import router as public_router
from .practica_session_controller import router as practica_router

__all__ = [
    "session_router",
    "recording_router",
    "fragment_router",
    "navigation_router",
    "public_router",
    "practica_router",
]
