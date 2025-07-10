from ...common.in_memory import InMemoryRepository
from ..models import GradeFeedback

_repo = InMemoryRepository[GradeFeedback]()

create_grade_feedback = _repo.create
list_grade_feedback = _repo.list
get_grade_feedback = _repo.get
update_grade_feedback = _repo.update
delete_grade_feedback = _repo.delete
