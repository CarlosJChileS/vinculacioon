from ...common.in_memory import InMemoryRepository
from ..models import Presentation

_repo = InMemoryRepository[Presentation]()

create_presentation = _repo.create
list_presentations = _repo.list
get_presentation = _repo.get
update_presentation = _repo.update
delete_presentation = _repo.delete
