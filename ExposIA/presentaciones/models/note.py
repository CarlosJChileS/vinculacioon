from pydantic import BaseModel

class SlideNote(BaseModel):
    id: int | None = None
    presentacion_id: int
    slide_id: int
    contenido: str
    timestamp: float
