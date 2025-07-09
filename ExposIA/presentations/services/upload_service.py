from pathlib import Path
from fastapi import UploadFile

UPLOAD_DIR = Path("data/presentations")


def save_presentation(uploaded: UploadFile) -> str:
    """Guarda el archivo de presentacion y devuelve la ruta."""
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    file_path = UPLOAD_DIR / uploaded.filename
    with file_path.open("wb") as buffer:
        buffer.write(uploaded.file.read())
    return str(file_path)
