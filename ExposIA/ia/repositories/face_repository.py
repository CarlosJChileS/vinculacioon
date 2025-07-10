"""Repositorio para guardar resultados de deteccion facial."""
from typing import List, Optional

from ..models.face import FaceRecord, FaceRecordOrm
from ...common.database import SessionLocal


def create_face(model: FaceRecord) -> FaceRecord:
    with SessionLocal() as session:
        obj = FaceRecordOrm(**model.model_dump(exclude={"id"}))
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return FaceRecord(**obj.__dict__)


def list_faces() -> List[FaceRecord]:
    with SessionLocal() as session:
        objs = session.query(FaceRecordOrm).all()
        return [FaceRecord(**o.__dict__) for o in objs]


def get_face(obj_id: int) -> Optional[FaceRecord]:
    with SessionLocal() as session:
        obj = session.get(FaceRecordOrm, obj_id)
        return FaceRecord(**obj.__dict__) if obj else None


def update_face(obj_id: int, model: FaceRecord) -> Optional[FaceRecord]:
    with SessionLocal() as session:
        obj = session.get(FaceRecordOrm, obj_id)
        if not obj:
            return None
        for k, v in model.model_dump(exclude={"id"}).items():
            setattr(obj, k, v)
        session.commit()
        return FaceRecord(**obj.__dict__)


def delete_face(obj_id: int) -> bool:
    with SessionLocal() as session:
        obj = session.get(FaceRecordOrm, obj_id)
        if not obj:
            return False
        session.delete(obj)
        session.commit()
        return True
