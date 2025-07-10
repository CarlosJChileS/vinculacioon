from pydantic import BaseModel

class Recording(BaseModel):
    id: int | None = None
    usuario_id: int
    presentacion_id: int
    archivo_audio: str
