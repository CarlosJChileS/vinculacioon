from .grading_controller import router as grading_router
from .grade_controller import router as grade_router
from .detail_controller import router as detail_router
from .criterion_controller import router as criterion_router
from .feedback_controller import router as grade_feedback_router
from .external_controller import router as external_router

__all__ = [
    "grading_router",
    "grade_router",
    "detail_router",
    "criterion_router",
    "grade_feedback_router",
    "external_router",
]
