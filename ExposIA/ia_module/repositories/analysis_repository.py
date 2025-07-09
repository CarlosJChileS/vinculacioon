"""Repositorio para manejar la persistencia de resultados."""
from ..models.analysis_result import AnalysisResultModel
from ...common.supabase_client import get_client

_memory: list[dict] = []


def save_result(result: AnalysisResultModel) -> AnalysisResultModel:
    """Guarda el resultado en Supabase o en memoria si no hay credenciales."""
    client = get_client()
    data = result.dict(exclude_none=True)
    if client:
        client.table("resultado_ia").insert(data).execute()
    else:
        result.id = len(_memory) + 1
        _memory.append(data)
    return result
