from ...common.in_memory import InMemoryRepository
from ..models import Recording

_repo = InMemoryRepository[Recording]()

create_recording = _repo.create
list_recordings = _repo.list
get_recording = _repo.get
update_recording = _repo.update
delete_recording = _repo.delete
