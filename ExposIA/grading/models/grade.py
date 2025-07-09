from pydantic import BaseModel

class Grade(BaseModel):
    id: int | None = None
    grabacion_id: int
    usuario_id: int
    puntaje_global: float
    observacion_global: str | None = None
