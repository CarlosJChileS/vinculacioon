"""Repositorio para manejar feedback textual."""
from ...common.in_memory import InMemoryRepository
from ..models.feedback import FeedbackModel

_repo = InMemoryRepository[FeedbackModel]()

create_feedback = _repo.create
list_feedback = _repo.list
get_feedback = _repo.get
update_feedback = _repo.update
delete_feedback = _repo.delete
