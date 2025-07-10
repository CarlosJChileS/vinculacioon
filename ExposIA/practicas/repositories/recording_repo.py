from fastapi import UploadFile
from pathlib import Path
from ...common.database import SessionLocal
from ..models.recording import Recording, RecordingOrm

UPLOAD_DIR = Path("data/recordings")


def create_recording(rec: Recording) -> Recording:
    with SessionLocal() as session:
        obj = RecordingOrm(**rec.model_dump(exclude={"id"}))
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return Recording(**obj.__dict__)


def list_recordings() -> list[Recording]:
    with SessionLocal() as session:
        objs = session.query(RecordingOrm).all()
        return [Recording(**o.__dict__) for o in objs]


def create_recording_from_file(usuario_id: int, presentacion_id: int, audio: UploadFile) -> Recording:
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    with SessionLocal() as session:
        obj = RecordingOrm(usuario_id=usuario_id, presentacion_id=presentacion_id, archivo_audio="")
        session.add(obj)
        session.commit()
        session.refresh(obj)
        dest = UPLOAD_DIR / f"{obj.id}.wav"
        with dest.open("wb") as fh:
            fh.write(audio.file.read())
        obj.archivo_audio = str(dest)
        session.commit()
        return Recording(**obj.__dict__)
