from pydantic import BaseModel
from sqlalchemy import Column, Integer, Float, String
from ...common.database import Base


class SlideNavigationOrm(Base):
    __tablename__ = "navegacion_slides"
    id = Column(Integer, primary_key=True, autoincrement=True)
    presentacion_id = Column(Integer)
    slide_id = Column(Integer)
    timestamp = Column(Float)
    tipo_navegacion = Column(String)

class SlideNavigation(BaseModel):
    id: int | None = None
    presentacion_id: int
    slide_id: int
    timestamp: float
    tipo_navegacion: str
