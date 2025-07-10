from ..models import SlideNavigation
from ..repositories.navigation_repo import (
    create_navigation, list_navigation
)

def add_navigation(data: SlideNavigation) -> SlideNavigation:
    return create_navigation(data)


def get_navigation():
    return list_navigation()
