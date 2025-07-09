"""Servicios de analisis de audio."""
from pathlib import Path

from ..ia_core.analysis import analyze_audio, Result
from ..dtos.analysis_dto import AudioAnalysisInput
from ..models.analysis_result import AnalysisResultModel
from ..models.feedback import FeedbackModel
from ..models.face import FaceRecord
from ..repositories.analysis_repository import create_result
from ..repositories.feedback_repository import create_feedback

try:
    from ..ia_extras.face_detection.detection import analyze_emotion
    from ..repositories.face_repository import create_face
except Exception:  # pragma: no cover
    analyze_emotion = None

RECORDINGS_DIR = Path("data/recordings")


def process_audio(data: AudioAnalysisInput) -> Result:
    """Procesa un archivo subido directamente."""
    return analyze_audio(data.content)


def process_recording(grabacion_id: str) -> Result:
    """Carga la grabacion desde disco, analiza y persiste el resultado."""
    file_path = RECORDINGS_DIR / f"{grabacion_id}.wav"
    if not file_path.exists():
        raise FileNotFoundError(str(file_path))
    content = file_path.read_bytes()
    result = analyze_audio(content)

    saved = create_result(AnalysisResultModel(**result.dict()))
    feedback = _generate_feedback(result)
    create_feedback(
        FeedbackModel(grabacion_id=int(grabacion_id), metrica_id=1, valor=0, comentario=feedback)
    )
    if analyze_emotion:
        face = analyze_emotion(b"")
        create_face(FaceRecord(resultado_id=saved.id or 0, emocion=face.emocion, confianza=face.confianza))
    return result


def _generate_feedback(result: Result) -> str:
    """Genera un texto simple de retroalimentacion."""
    if result.velocidad_palabras > 150:
        return "Habla un poco mas despacio"
    return "Buen ritmo"
