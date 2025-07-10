from pydantic import BaseModel

class Criterion(BaseModel):
    id: int | None = None
    nombre: str
    peso: float
