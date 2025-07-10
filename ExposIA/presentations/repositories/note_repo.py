from ...common.in_memory import InMemoryRepository
from ..models import SlideNote

_repo = InMemoryRepository[SlideNote]()

create_note = _repo.create
list_notes = _repo.list
get_note = _repo.get
update_note = _repo.update
delete_note = _repo.delete
