"""Servicio de practicas."""
from ...common.supabase_client import get_client


def register_navigation() -> str:
    """Ejemplo de registro de navegacion en Supabase o memoria."""
    client = get_client()
    data = {"mensaje": "navegacion"}
    if client:
        client.table("navegacion_slides").insert(data).execute()
    return "registro guardado"
