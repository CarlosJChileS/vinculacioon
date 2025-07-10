from pydantic import BaseModel

class PracticeSession(BaseModel):
    id: int | None = None
    usuario_id: int
    presentacion_id: int
    fecha: float
