from ...common.database import SessionLocal
from ..models.slide_nav import SlideNavigation, SlideNavigationOrm


def create_navigation(nav: SlideNavigation) -> SlideNavigation:
    with SessionLocal() as session:
        obj = SlideNavigationOrm(**nav.model_dump(exclude={"id"}))
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return SlideNavigation(**obj.__dict__)


def list_navigation() -> list[SlideNavigation]:
    with SessionLocal() as session:
        objs = session.query(SlideNavigationOrm).all()
        return [SlideNavigation(**o.__dict__) for o in objs]


def get_navigation(nav_id: int) -> SlideNavigation | None:
    with SessionLocal() as session:
        obj = session.get(SlideNavigationOrm, nav_id)
        return SlideNavigation(**obj.__dict__) if obj else None


def update_navigation(nav_id: int, nav: SlideNavigation) -> SlideNavigation | None:
    with SessionLocal() as session:
        obj = session.get(SlideNavigationOrm, nav_id)
        if not obj:
            return None
        for f, v in nav.model_dump(exclude={"id"}).items():
            setattr(obj, f, v)
        session.commit()
        return SlideNavigation(**obj.__dict__)


def delete_navigation(nav_id: int) -> bool:
    with SessionLocal() as session:
        obj = session.get(SlideNavigationOrm, nav_id)
        if not obj:
            return False
        session.delete(obj)
        session.commit()
        return True
