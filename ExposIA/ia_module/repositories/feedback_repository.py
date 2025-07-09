"""Repositorio para guardar feedback textual."""
from typing import Optional
from ...common.supabase_client import get_client

_memory: list[dict] = []


def save_feedback(result_id: int, texto: str) -> None:
    """Guarda el feedback en Supabase o en memoria."""
    client = get_client()
    data = {"resultado_id": result_id, "texto": texto}
    if client:
        client.table("feedback").insert(data).execute()
    else:
        _memory.append(data)
