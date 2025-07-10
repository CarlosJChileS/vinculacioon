from fastapi import APIRouter
from ..models import SlideNavigation
from ..services.navigation_service import add_navigation, get_navigation

router = APIRouter(prefix="/navigation")

@router.post("/", response_model=SlideNavigation)
async def create_nav_route(nav: SlideNavigation):
    return add_navigation(nav)

@router.get("/", response_model=list[SlideNavigation])
async def list_nav_route():
    return get_navigation()
