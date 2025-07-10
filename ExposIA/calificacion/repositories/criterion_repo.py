from ...common.in_memory import InMemoryRepository
from ..models import Criterion

_repo = InMemoryRepository[Criterion]()

create_criterion = _repo.create
list_criteria = _repo.list
get_criterion = _repo.get
update_criterion = _repo.update
delete_criterion = _repo.delete
