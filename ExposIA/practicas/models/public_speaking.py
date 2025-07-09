from pydantic import BaseModel

class PublicSpeakingSession(BaseModel):
    id: int | None = None
    grabacion_id: int
    distancia_total: float
    fecha_inicio: float
    fecha_fin: float
    finalizada: bool = False
