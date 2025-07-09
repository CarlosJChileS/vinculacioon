"""Servicios de analisis de audio."""
from ..ia_core.analysis import analyze_audio, Result
from ..dtos.analysis_dto import AudioAnalysisInput


def process_audio(data: AudioAnalysisInput) -> Result:
    """Procesa el audio usando las funciones del core."""
    return analyze_audio(data.

