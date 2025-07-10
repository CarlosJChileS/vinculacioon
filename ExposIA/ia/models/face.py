from pydantic import BaseModel
from sqlalchemy import Column, Integer, Float, String
from ...common.database import Base


class FaceRecordOrm(Base):
    __tablename__ = "deteccion_facial"
    id = Column(Integer, primary_key=True, autoincrement=True)
    resultado_id = Column(Integer)
    emocion = Column(String)
    confianza = Column(Float)

class FaceRecord(BaseModel):
    id: int | None = None
    resultado_id: int
    emocion: str
    confianza: float
