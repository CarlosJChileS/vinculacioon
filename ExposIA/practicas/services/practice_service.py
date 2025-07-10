"""Servicio de practicas."""
from ..models.slide_nav import SlideNavigationOrm
from ...common.database import SessionLocal


def register_navigation() -> str:
    """Ejemplo de registro de navegacion en Supabase o memoria."""
    with SessionLocal() as session:
        nav = SlideNavigationOrm(presentacion_id=1, slide_id=1, timestamp=0.0, tipo_navegacion="start")
        session.add(nav)
        session.commit()
    return "registro guardado"
