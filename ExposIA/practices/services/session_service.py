from ..models import PracticeSession
from ..repositories.session_repo import (
    create_session, list_sessions
)

def add_session(data: PracticeSession) -> PracticeSession:
    return create_session(data)


def get_sessions():
    return list_sessions()
