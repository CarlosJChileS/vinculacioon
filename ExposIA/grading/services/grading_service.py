from ..dtos.grading_dto import GradingInput, GradingResult


def grade_practice(data: GradingInput) -> GradingResult:
    """Genera una nota simple a partir de las metricas."""
    # Algoritmo ficticio
    score = (
        data.velocidad_palabras / 200.0 * 0.4 +
        data.claridad * 0.4 +
        max(0.0, 1 - data.num_pausas / 10) * 0.2
    ) * 100
    return GradingResult(nota_global=round(score, 2))
