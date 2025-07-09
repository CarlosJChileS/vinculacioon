from pydantic import BaseModel

class GradingInput(BaseModel):
    velocidad_palabras: float
    claridad: float
    num_pausas: int

class GradingResult(BaseModel):
    nota_global: float
