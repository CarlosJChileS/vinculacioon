from ...common.in_memory import InMemoryRepository
from ..models import SesionPractica

_repo = InMemoryRepository[SesionPractica]()

create_session = _repo.create
list_sessions = _repo.list
get_session = _repo.get
update_session = _repo.update
delete_session = _repo.delete
