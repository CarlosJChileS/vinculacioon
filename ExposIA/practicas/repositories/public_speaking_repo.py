from ...common.in_memory import InMemoryRepository
from ..models import PublicSpeakingSession

_repo = InMemoryRepository[PublicSpeakingSession]()

create_public = _repo.create
list_public = _repo.list
get_public = _repo.get
update_public = _repo.update
delete_public = _repo.delete
