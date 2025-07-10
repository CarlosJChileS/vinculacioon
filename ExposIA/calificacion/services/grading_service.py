from ..dtos.grading_dto import GradingInput, GradingResult
from ..models.grade import GradeOrm
from ...common.database import SessionLocal
def grade_practice(data: GradingInput) -> GradingResult:
    """Genera una nota simple a partir de las metricas."""
    # Algoritmo ficticio
    score = (
        data.velocidad_palabras / 200.0 * 0.4 +
        data.claridad * 0.4 +
        max(0.0, 1 - data.num_pausas / 10) * 0.2
    ) * 100
    result = GradingResult(nota_global=round(score, 2))
    with SessionLocal() as session:
        grade = GradeOrm(grabacion_id=1, usuario_id=1, puntaje_global=result.nota_global)
        session.add(grade)
        session.commit()
    return result
