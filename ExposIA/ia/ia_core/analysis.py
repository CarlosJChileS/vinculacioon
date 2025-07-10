"""Funciones principales de analisis de audio y texto utilizando Whisper local."""

from pathlib import Path
from tempfile import NamedTemporaryFile

import librosa
import whisper
from pydantic import BaseModel


class Result(BaseModel):
    velocidad_palabras: float
    claridad: float
    num_pausas: int
    retroalimentacion: str


_model = None


def _load_model():
    """Carga el modelo de Whisper solo una vez."""
    global _model
    if _model is None:
        _model = whisper.load_model("tiny")
    return _model


def analyze_audio(audio_bytes: bytes) -> Result:
    """Analiza el audio con Whisper y Librosa."""
    with NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        tmp.write(audio_bytes)
        tmp.flush()
        path = Path(tmp.name)

    result = _load_model().transcribe(str(path))
    texto_transcrito = result["text"]

    y, sr = librosa.load(path, sr=None)
    duration = librosa.get_duration(y=y, sr=sr) or 1.0
    words = len(texto_transcrito.split())
    velocidad = words / (duration / 60)
    intervals = librosa.effects.split(y, top_db=30)
    num_pausas = max(len(intervals) - 1, 0)
    claridad = max(0.1, 1 - num_pausas / 10)

    path.unlink(missing_ok=True)

    retro = "Habla un poco más despacio" if velocidad > 160 else "Buen ritmo"

    return Result(
        velocidad_palabras=velocidad,
        claridad=claridad,
        num_pausas=num_pausas,
        retroalimentacion=retro,
    )
