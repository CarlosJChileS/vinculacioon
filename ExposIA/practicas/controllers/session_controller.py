from fastapi import APIRouter
from ..services.practica_service import register_navigation

router = APIRouter()

@router.get("/status")
async def get_status():
    return {"status": register_navigation()}
