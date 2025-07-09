from pydantic import BaseModel

class MetricType(BaseModel):
    id: int | None = None
    nombre: str
    descripcion: str | None = None

class Metric(BaseModel):
    id: int | None = None
    nombre: str
    descripcion: str | None = None
    tipo_metrica_id: int

class Parameter(BaseModel):
    id: int | None = None
    metrica_id: int
    valor: float
    umbral: float
