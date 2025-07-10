from fastapi import UploadFile
from ..models import Recording
from ..repositories.recording_repo import (
    create_recording, list_recordings, create_recording_from_file
)

def add_recording(data: Recording) -> Recording:
    return create_recording(data)


def get_recordings():
    return list_recordings()


def add_recording_file(usuario_id: int, presentacion_id: int, audio: UploadFile) -> Recording:
    return create_recording_from_file(usuario_id, presentacion_id, audio)
