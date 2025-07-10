from pydantic import BaseModel

class SesionPractica(BaseModel):
    id: int | None = None
    usuario_id: int
    presentacion_id: int
    fecha: float
