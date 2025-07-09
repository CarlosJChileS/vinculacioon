from pydantic import BaseModel

class FaceRecord(BaseModel):
    id: int | None = None
    resultado_id: int
    emocion: str
    confianza: float
