"""Repositorio para manejar resultados de analisis de audio."""
from ..models.analysis_result import AnalysisResultModel
from ...common.in_memory import InMemoryRepository

_repo = InMemoryRepository[AnalysisResultModel]()

create_result = _repo.create
list_results = _repo.list
get_result = _repo.get
update_result = _repo.update
delete_result = _repo.delete
