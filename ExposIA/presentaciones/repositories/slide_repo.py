from ...common.database import SessionLocal
from ..models.slide import Slide, SlideOrm


def create_slide(slide: Slide) -> Slide:
    with SessionLocal() as session:
        obj = SlideOrm(**slide.model_dump(exclude={"id"}))
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return Slide(**obj.__dict__)


def list_slides() -> list[Slide]:
    with SessionLocal() as session:
        objs = session.query(SlideOrm).all()
        return [Slide(**o.__dict__) for o in objs]


def get_slide(slide_id: int) -> Slide | None:
    with SessionLocal() as session:
        obj = session.get(SlideOrm, slide_id)
        return Slide(**obj.__dict__) if obj else None


def update_slide(slide_id: int, slide: Slide) -> Slide | None:
    with SessionLocal() as session:
        obj = session.get(SlideOrm, slide_id)
        if not obj:
            return None
        for f, v in slide.model_dump(exclude={"id"}).items():
            setattr(obj, f, v)
        session.commit()
        return Slide(**obj.__dict__)


def delete_slide(slide_id: int) -> bool:
    with SessionLocal() as session:
        obj = session.get(SlideOrm, slide_id)
        if not obj:
            return False
        session.delete(obj)
        session.commit()
        return True
