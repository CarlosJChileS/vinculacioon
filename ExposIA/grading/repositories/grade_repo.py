from ...common.in_memory import InMemoryRepository
from ..models import Grade

_repo = InMemoryRepository[Grade]()

create_grade = _repo.create
list_grades = _repo.list
get_grade = _repo.get
update_grade = _repo.update
delete_grade = _repo.delete
