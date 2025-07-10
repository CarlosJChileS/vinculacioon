from ...common.in_memory import InMemoryRepository
from ..models import User

_repo = InMemoryRepository[User]()

create_user = _repo.create
list_users = _repo.list
get_user = _repo.get
update_user = _repo.update
delete_user = _repo.delete
