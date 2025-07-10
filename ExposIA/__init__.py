"""Paquete principal de ExposIA."""
from .ia.main import app as ia_app
from .common.database import init_db

init_db()

__all__ = ["ia_app"]
