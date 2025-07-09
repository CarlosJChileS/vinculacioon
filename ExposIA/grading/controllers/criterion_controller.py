from fastapi import APIRouter
from ..models import Criterion
from ..services.criterion_service import add_criterion, get_criteria

router = APIRouter(prefix="/criteria")

@router.post("/", response_model=Criterion)
async def create_criterion_route(c: Criterion):
    return add_criterion(c)

@router.get("/", response_model=list[Criterion])
async def list_criteria_route():
    return get_criteria()
