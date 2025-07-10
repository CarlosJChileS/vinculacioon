from ..models import Presentation
from ..repositories.presentation_repo import (
    create_presentation, list_presentations, get_presentation, update_presentation, delete_presentation
)


def add_presentation(data: Presentation) -> Presentation:
    return create_presentation(data)


def get_presentations():
    return list_presentations()
