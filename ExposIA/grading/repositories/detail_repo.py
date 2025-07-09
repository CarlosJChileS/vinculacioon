from ...common.in_memory import InMemoryRepository
from ..models import GradeDetail

_repo = InMemoryRepository[GradeDetail]()

create_detail = _repo.create
list_details = _repo.list
get_detail = _repo.get
update_detail = _repo.update
delete_detail = _repo.delete
