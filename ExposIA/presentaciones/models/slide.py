from pydantic import BaseModel

class Slide(BaseModel):
    id: int | None = None
    presentacion_id: int
    numero_slide: int
    img_slide: str | None = None
    texto_slide: str | None = None
