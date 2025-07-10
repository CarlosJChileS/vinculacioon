from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from ...common.database import Base


class RecordingOrm(Base):
    __tablename__ = "grabaciones"
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer)
    presentacion_id = Column(Integer)
    archivo_audio = Column(String)

class Recording(BaseModel):
    id: int | None = None
    usuario_id: int
    presentacion_id: int
    archivo_audio: str
