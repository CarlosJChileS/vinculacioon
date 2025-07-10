from ...common.in_memory import InMemoryRepository
from ..models import PracticeSession

_repo = InMemoryRepository[PracticeSession]()

create_session = _repo.create
list_sessions = _repo.list
get_session = _repo.get
update_session = _repo.update
delete_session = _repo.delete
