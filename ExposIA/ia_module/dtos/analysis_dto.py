from pydantic import BaseModel

class AnalysisResult(BaseModel):
    """DTO para resultados del analisis de audio."""
    velocidad_palabras: float
    claridad: float
    num_pausas: int
    retroalimentacion: str
