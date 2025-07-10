from ...common.in_memory import InMemoryRepository
from ..models import Slide

_repo = InMemoryRepository[Slide]()

create_slide = _repo.create
list_slides = _repo.list
get_slide = _repo.get
update_slide = _repo.update
delete_slide = _repo.delete
