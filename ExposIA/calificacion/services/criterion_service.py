from ..models import Criterion
from ..repositories.criterion_repo import create_criterion, list_criteria

def add_criterion(data: Criterion) -> Criterion:
    return create_criterion(data)

def get_criteria():
    return list_criteria()
