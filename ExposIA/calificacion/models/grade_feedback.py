from pydantic import BaseModel

class GradeFeedback(BaseModel):
    id: int | None = None
    calificacion_id: int
    observacion: str
    fecha: float
    autor: str
