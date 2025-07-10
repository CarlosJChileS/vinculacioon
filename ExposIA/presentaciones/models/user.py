from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from ...common.database import Base


class UserOrm(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

class User(BaseModel):
    id: int | None = None
    nombre: str
    email: str
    password: str
