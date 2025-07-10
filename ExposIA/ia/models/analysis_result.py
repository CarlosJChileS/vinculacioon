"""Modelos de dominio utilizados de manera local."""
from pydantic import BaseModel, Field


class AnalysisResultModel(BaseModel):
    """Representa un resultado de an\u00e1lisis sin persistencia."""

    id: int | None = Field(default=None, description="Identificador opcional")
    velocidad_palabras: float
    claridad: float
    num_pausas: int
    retroalimentacion: str


class AudioInput(BaseModel):
    """Datos de entrada de audio para procesamiento."""

    filename: str
    content: bytes
