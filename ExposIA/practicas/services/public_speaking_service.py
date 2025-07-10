from ..models import PublicSpeakingSession
from ..repositories.public_speaking_repo import (
    create_public, list_public
)

def add_public(data: PublicSpeakingSession) -> PublicSpeakingSession:
    return create_public(data)


def get_public_sessions():
    return list_public()
