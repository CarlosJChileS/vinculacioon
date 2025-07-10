from ..models import GradeFeedback
from ..repositories.feedback_repo import create_grade_feedback, list_grade_feedback

def add_grade_feedback(data: GradeFeedback) -> GradeFeedback:
    return create_grade_feedback(data)

def get_grade_feedbacks():
    return list_grade_feedback()
