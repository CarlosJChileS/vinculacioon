from pydantic import BaseModel

class GradeDetail(BaseModel):
    id: int | None = None
    calificacion_id: int
    criterio_id: int
    valor: float
    comentario: str | None = None
