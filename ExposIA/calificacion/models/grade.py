from pydantic import BaseModel
from sqlalchemy import Column, Integer, Float, String
from ...common.database import Base


class GradeOrm(Base):
    __tablename__ = "calificaciones"
    id = Column(Integer, primary_key=True, autoincrement=True)
    grabacion_id = Column(Integer)
    usuario_id = Column(Integer)
    puntaje_global = Column(Float)
    observacion_global = Column(String)

class Grade(BaseModel):
    id: int | None = None
    grabacion_id: int
    usuario_id: int
    puntaje_global: float
    observacion_global: str | None = None
