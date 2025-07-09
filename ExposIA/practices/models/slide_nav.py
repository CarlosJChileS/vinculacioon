from pydantic import BaseModel

class SlideNavigation(BaseModel):
    id: int | None = None
    presentacion_id: int
    slide_id: int
    timestamp: float
    tipo_navegacion: str
