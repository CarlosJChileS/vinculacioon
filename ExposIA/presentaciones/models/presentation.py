from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from ...common.database import Base


class PresentationOrm(Base):
    __tablename__ = "presentaciones"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tema_id = Column(Integer)
    usuario_id = Column(Integer)
    archivo_pdf = Column(String)

class Presentation(BaseModel):
    id: int | None = None
    tema_id: int
    usuario_id: int
    archivo_pdf: str
