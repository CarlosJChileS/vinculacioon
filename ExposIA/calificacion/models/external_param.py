from pydantic import BaseModel

class ExternalParam(BaseModel):
    id: int | None = None
    calidad_ideal: str
    valor_actual: str
    razones_breves: str | None = None
    otros_parametros: str | None = None
