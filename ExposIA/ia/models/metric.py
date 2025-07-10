from pydantic import BaseModel
from sqlalchemy import Column, Integer, Float, String
from ...common.database import Base


class MetricTypeOrm(Base):
    __tablename__ = "tipo_metrica"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    descripcion = Column(String)


class MetricOrm(Base):
    __tablename__ = "metrica"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    descripcion = Column(String)
    tipo_metrica_id = Column(Integer)


class ParameterOrm(Base):
    __tablename__ = "parametro"
    id = Column(Integer, primary_key=True, autoincrement=True)
    metrica_id = Column(Integer)
    valor = Column(Float)
    umbral = Column(Float)

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
