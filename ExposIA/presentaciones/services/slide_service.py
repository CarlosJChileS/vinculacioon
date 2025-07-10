from ..models import Slide, SlideNote
from ..repositories.slide_repo import (
    create_slide, list_slides, get_slide, update_slide, delete_slide
)
from ..repositories.note_repo import (
    create_note, list_notes, get_note, update_note, delete_note
)


def add_slide(data: Slide) -> Slide:
    return create_slide(data)


def get_slides():
    return list_slides()


def add_note(data: SlideNote) -> SlideNote:
    return create_note(data)


def get_notes():
    return list_notes()
