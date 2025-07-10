from pydantic import BaseModel

class MetricTypeDTO(BaseModel):
    id: int | None = None
    nombre: str
    descripcion: str | None = None

class MetricDTO(BaseModel):
    id: int | None = None
    nombre: str
    descripcion: str | None = None
    tipo_metrica_id: int

class ParameterDTO(BaseModel):
    id: int | None = None
    metrica_id: int
    valor: float
    umbral: float
