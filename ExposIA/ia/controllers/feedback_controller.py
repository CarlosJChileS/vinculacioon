from fastapi import APIRouter
from ..dtos.feedback_dto import FeedbackDTO
from ..services.feedback_service import add_feedback, list_all_feedback

router = APIRouter(prefix="/feedback")

@router.post("/", response_model=FeedbackDTO)
async def create_feedback_route(data: FeedbackDTO):
    return add_feedback(data)

@router.get("/", response_model=list[FeedbackDTO])
async def list_feedback_route():
    return list_all_feedback()
