from ..models import ExternalParam
from ..repositories.external_repo import create_external, list_external

def add_external(data: ExternalParam) -> ExternalParam:
    return create_external(data)

def get_external_params():
    return list_external()
