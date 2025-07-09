from fastapi import APIRouter
from ..models import GradeFeedback
from ..services.feedback_service import add_grade_feedback, get_grade_feedbacks

router = APIRouter(prefix="/grade-feedback")

@router.post("/", response_model=GradeFeedback)
async def create_feedback_route(f: GradeFeedback):
    return add_grade_feedback(f)

@router.get("/", response_model=list[GradeFeedback])
async def list_feedback_route():
    return get_grade_feedbacks()
