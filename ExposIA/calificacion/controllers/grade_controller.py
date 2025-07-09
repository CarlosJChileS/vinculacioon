from fastapi import APIRouter
from ..models import Grade
from ..services.grade_service import add_grade, get_grades

router = APIRouter(prefix="/grades")

@router.post("/", response_model=Grade)
async def create_grade_route(g: Grade):
    return add_grade(g)

@router.get("/", response_model=list[Grade])
async def list_grades_route():
    return get_grades()
