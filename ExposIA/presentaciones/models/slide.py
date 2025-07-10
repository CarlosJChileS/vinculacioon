from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from ...common.database import Base


class SlideOrm(Base):
    __tablename__ = "slides"
    id = Column(Integer, primary_key=True, autoincrement=True)
    presentacion_id = Column(Integer)
    numero_slide = Column(Integer)
    img_slide = Column(String)
    texto_slide = Column(String)

class Slide(BaseModel):
    id: int | None = None
    presentacion_id: int
    numero_slide: int
    img_slide: str | None = None
    texto_slide: str | None = None
