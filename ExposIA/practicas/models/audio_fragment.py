from pydantic import BaseModel

class AudioFragment(BaseModel):
    id: int | None = None
    grabacion_id: int
    slide_id: int
    inicio_segundo: int
    fin_segundo: int
    archivo_fragmento: str
