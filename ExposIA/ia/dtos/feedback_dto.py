from pydantic import BaseModel

class FeedbackDTO(BaseModel):
    id: int | None = None
    grabacion_id: int
    metrica_id: int
    valor: float
    comentario: str
    es_manual: bool = False
