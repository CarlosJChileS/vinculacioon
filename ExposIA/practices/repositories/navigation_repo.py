from ...common.in_memory import InMemoryRepository
from ..models import SlideNavigation

_repo = InMemoryRepository[SlideNavigation]()

create_navigation = _repo.create
list_navigation = _repo.list
get_navigation = _repo.get
update_navigation = _repo.update
delete_navigation = _repo.delete
