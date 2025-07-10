from pathlib import Path
from fastapi import UploadFile
from ..dtos.presentation_dto import PresentationInfo
from ..models.presentation import PresentationOrm
from ...common.database import SessionLocal

UPLOAD_DIR = Path("data/presentations")


def save_presentation(uploaded: UploadFile) -> PresentationInfo:
    """Guarda el archivo de presentacion y registra la metadata."""
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    file_path = UPLOAD_DIR / uploaded.filename
    with file_path.open("wb") as buffer:
        buffer.write(uploaded.file.read())
    with SessionLocal() as session:
        obj = PresentationOrm(tema_id=1, usuario_id=1, archivo_pdf=str(file_path))
        session.add(obj)
        session.commit()
    return PresentationInfo(filename=uploaded.filename, stored_at=str(file_path))
