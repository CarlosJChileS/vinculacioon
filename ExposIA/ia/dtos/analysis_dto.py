from pydantic import BaseModel

class AudioAnalysisInput(BaseModel):
    """DTO de entrada para analizar audio."""

    filename: str
    content: bytes


class AnalysisResult(BaseModel):
    """DTO para resultados del analisis de audio."""

    velocidad_palabras: float
    claridad: float
    num_pausas: int
    retroalimentacion: str
