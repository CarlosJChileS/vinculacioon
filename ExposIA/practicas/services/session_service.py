from ..models import SesionPractica
from ..repositories.session_repo import (
    create_session, list_sessions
)

def add_session(data: SesionPractica) -> SesionPractica:
    return create_session(data)


def get_sessions():
    return list_sessions()
