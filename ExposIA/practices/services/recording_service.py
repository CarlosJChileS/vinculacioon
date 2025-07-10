from ..models import Recording
from ..repositories.recording_repo import (
    create_recording, list_recordings
)

def add_recording(data: Recording) -> Recording:
    return create_recording(data)


def get_recordings():
    return list_recordings()
