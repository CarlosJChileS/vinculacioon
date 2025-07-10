"""Funciones de mapeo entre modelos y dtos."""
from ..ia_core.analysis import Result
from ..dtos.analysis_dto import AnalysisResult


def to_dto(result: Result) -> AnalysisResult:
    return AnalysisResult(
        velocidad_palabras=result.velocidad_palabras,
        claridad=result.claridad,
        num_pausas=result.num_pausas,
        retroalimentacion=result.retroalimentacion,
    )
