"""Modelos de dominio utilizados de manera local."""
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, Float, String
from ...common.database import Base


class AnalysisResult(Base):
    __tablename__ = "resultado_ia"
    id = Column(Integer, primary_key=True, autoincrement=True)
    velocidad_palabras = Column(Float)
    claridad = Column(Float)
    num_pausas = Column(Integer)
    retroalimentacion = Column(String)


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
