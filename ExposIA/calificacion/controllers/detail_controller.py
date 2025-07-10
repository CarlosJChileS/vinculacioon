from fastapi import APIRouter
from ..models import GradeDetail
from ..services.detail_service import add_detail, get_details

router = APIRouter(prefix="/grade-details")

@router.post("/", response_model=GradeDetail)
async def create_detail_route(d: GradeDetail):
    return add_detail(d)

@router.get("/", response_model=list[GradeDetail])
async def list_details_route():
    return get_details()
