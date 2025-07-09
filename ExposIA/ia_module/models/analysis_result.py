"""Modelo ORM para almacenar resultados de analisis."""
from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AnalysisResultModel(Base):
    __tablename__ = "resultado_ia"

    id = Column(Integer, primary_key=True, autoincrement=True)
    velocidad_palabras = Column(Float)
    claridad = Column(Float)
    num_pausas = Column(Integer)
    retroalimentacion = Column(String)
