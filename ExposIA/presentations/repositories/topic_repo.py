from ...common.in_memory import InMemoryRepository
from ..models import Topic

_repo = InMemoryRepository[Topic]()

create_topic = _repo.create
list_topics = _repo.list
get_topic = _repo.get
update_topic = _repo.update
delete_topic = _repo.delete
