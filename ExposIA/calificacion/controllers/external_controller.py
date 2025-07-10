from fastapi import APIRouter
from ..models import ExternalParam
from ..services.external_service import add_external, get_external_params

router = APIRouter(prefix="/external-params")

@router.post("/", response_model=ExternalParam)
async def create_external_route(e: ExternalParam):
    return add_external(e)

@router.get("/", response_model=list[ExternalParam])
async def list_external_route():
    return get_external_params()
