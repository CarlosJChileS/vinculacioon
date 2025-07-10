from ...common.in_memory import InMemoryRepository
from ..models import ExternalParam

_repo = InMemoryRepository[ExternalParam]()

create_external = _repo.create
list_external = _repo.list
get_external = _repo.get
update_external = _repo.update
delete_external = _repo.delete
