"""Repositorio para guardar resultados de deteccion facial."""
from ...common.in_memory import InMemoryRepository
from ..models.face import FaceRecord

_repo = InMemoryRepository[FaceRecord]()

create_face = _repo.create
list_faces = _repo.list
get_face = _repo.get
update_face = _repo.update
delete_face = _repo.delete
