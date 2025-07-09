import os
from typing import Optional

try:
    from supabase import create_client, Client
except Exception:  # library may not be installed
    Client = None
    def create_client(url: str, key: str):
        raise RuntimeError("supabase-py is not installed")

_client: Optional[Client] = None


def get_client() -> Optional[Client]:
    """Return a Supabase client if credentials are configured."""
    global _client
    if _client is not None:
        return _client
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    if url and key and Client is not None:
        _client = create_client(url, key)
    return _client
