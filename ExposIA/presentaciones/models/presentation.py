from pydantic import BaseModel

class Presentation(BaseModel):
    id: int | None = None
    tema_id: int
    usuario_id: int
    archivo_pdf: str
