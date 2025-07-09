import pytest
from ExposIA.ia_module.services.audio_service import process_audio
from ExposIA.ia_module.dtos.analysis_dto import AudioAnalysisInput


def test_process_audio_returns_result():
    data = AudioAnalysisInput(filename="sample.wav", content=b"dummy")
    result = process_audio(data)
    assert result.velocidad_palabras > 0
    assert result.claridad > 0
    assert isinstance(result.num_pausas, int)

