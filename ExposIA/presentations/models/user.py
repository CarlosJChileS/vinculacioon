from pydantic import BaseModel

class User(BaseModel):
    id: int | None = None
    nombre: str
    email: str
    password: str
