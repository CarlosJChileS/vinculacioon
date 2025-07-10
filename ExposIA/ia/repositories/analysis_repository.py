"""Repositorio para manejar resultados de analisis de audio."""
from typing import List, Optional

from sqlalchemy.orm import Session

from ..models.analysis_result import AnalysisResultModel, AnalysisResult
from ...common.database import SessionLocal


def create_result(model: AnalysisResultModel) -> AnalysisResultModel:
    with SessionLocal() as session:
        obj = AnalysisResult(**model.model_dump(exclude={"id"}))
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return AnalysisResultModel(**obj.__dict__)


def list_results() -> List[AnalysisResultModel]:
    with SessionLocal() as session:
        objs = session.query(AnalysisResult).all()
        return [AnalysisResultModel(**o.__dict__) for o in objs]


def get_result(obj_id: int) -> Optional[AnalysisResultModel]:
    with SessionLocal() as session:
        obj = session.get(AnalysisResult, obj_id)
        return AnalysisResultModel(**obj.__dict__) if obj else None


def update_result(obj_id: int, model: AnalysisResultModel) -> Optional[AnalysisResultModel]:
    with SessionLocal() as session:
        obj = session.get(AnalysisResult, obj_id)
        if not obj:
            return None
        for field, value in model.model_dump(exclude={"id"}).items():
            setattr(obj, field, value)
        session.commit()
        return AnalysisResultModel(**obj.__dict__)


def delete_result(obj_id: int) -> bool:
    with SessionLocal() as session:
        obj = session.get(AnalysisResult, obj_id)
        if not obj:
            return False
        session.delete(obj)
        session.commit()
        return True

