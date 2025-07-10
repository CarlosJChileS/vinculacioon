from pydantic import BaseModel
from sqlalchemy import Column, Integer, Float, String, Boolean
from ...common.database import Base


class Feedback(Base):
    __tablename__ = "feedback"
    id = Column(Integer, primary_key=True, autoincrement=True)
    grabacion_id = Column(Integer)
    metrica_id = Column(Integer)
    valor = Column(Float)
    comentario = Column(String)
    es_manual = Column(Boolean, default=False)

class FeedbackModel(BaseModel):
    id: int | None = None
    grabacion_id: int
    metrica_id: int
    valor: float
    comentario: str
    es_manual: bool = False
