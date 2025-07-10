from ...common.in_memory import InMemoryRepository
from ..models import AudioFragment

_repo = InMemoryRepository[AudioFragment]()

create_fragment = _repo.create
list_fragments = _repo.list
get_fragment = _repo.get
update_fragment = _repo.update
delete_fragment = _repo.delete
