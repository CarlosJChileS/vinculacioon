from pathlib import Path
from fastapi import UploadFile
from ...common.supabase_client import get_client
from ..dtos.presentation_dto import PresentationInfo



UPLOAD_DIR = Path("data/presentations")


def save_presentation(uploaded: UploadFile) -> PresentationInfo:
    """Guarda el archivo de presentacion y registra la metadata."""
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    file_path = UPLOAD_DIR / uploaded.filename
    with file_path.open("wb") as buffer:
        buffer.write(uploaded.file.read())
    client = get_client()
    data = {"filename": uploaded.filename, "path": str(file_path)}
    if client:
        client.table("presentaciones").insert(data).execute()
    return PresentationInfo(filename=uploaded.filename, stored_at=str(file_path))
