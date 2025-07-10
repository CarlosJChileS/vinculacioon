from ..models import AudioFragment
from ..repositories.fragment_repo import (
    create_fragment, list_fragments
)

def add_fragment(data: AudioFragment) -> AudioFragment:
    return create_fragment(data)


def get_fragments():
    return list_fragments()
