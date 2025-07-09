"""Repositorio para manejar la persistencia de resultados."""
from sqlalchemy.orm import Session
from ..models.analysis_result import AnalysisResultModel


def save_result(db: Session, result: AnalysisResultModel) -> AnalysisResultModel:
    db.add(result)
    db.commit()
    db.refresh(result)
    return result
