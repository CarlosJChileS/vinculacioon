import pytest
from ExposIA.ia.services.audio_service import process_audio, process_recording, RECORDINGS_DIR
from ExposIA.ia.dtos.analysis_dto import AudioAnalysisInput


def test_process_audio_returns_result():
    data = AudioAnalysisInput(filename="sample.wav", content=b"dummy")
    result = process_audio(data)
    assert result.velocidad_palabras > 0
    assert result.claridad > 0
    assert isinstance(result.num_pausas, int)


def test_process_recording(tmp_path):
    RECORDINGS_DIR.mkdir(parents=True, exist_ok=True)
    audio_path = RECORDINGS_DIR / "123.wav"
    audio_path.write_bytes(b"dummy")
    result = process_recording("123")
    assert result.velocidad_palabras > 0
    assert result.claridad > 0


