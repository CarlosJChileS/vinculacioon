from fastapi import APIRouter
from ..dtos.grading_dto import GradingInput, GradingResult
from ..services.grading_service import grade_practice

router = APIRouter()

@router.post("/", response_model=GradingResult)
async def grade(data: GradingInput):
    return grade_practice(data)
