"""Repositorio para guardar resultados de deteccion facial."""
from ...common.supabase_client import get_client

_memory: list[dict] = []


def save_face_result(result_id: int, emocion: str, confianza: float) -> None:
    """Guarda la emocion dominante asociada a un resultado."""
    client = get_client()
    data = {"resultado_id": result_id, "emocion": emocion, "confianza": confianza}
    if client:
        client.table("deteccion_facial").insert(data).execute()
    else:
        _memory.append(data)
