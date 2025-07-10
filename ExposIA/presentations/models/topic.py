from pydantic import BaseModel

class Topic(BaseModel):
    id: int | None = None
    nombre: str
    descripcion: str | None = None
