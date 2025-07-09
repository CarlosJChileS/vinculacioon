"""Servicios de analisis de audio."""
from ..ia_core.analysis import analyze_audio, Result


def process_audio(audio_bytes: bytes) -> Result:
    """Procesa el audio usando las funciones del core."""
    return analyze_audio(audio_bytes)
