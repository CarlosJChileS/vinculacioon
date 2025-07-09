from ..models import Grade
from ..repositories.grade_repo import create_grade, list_grades

def add_grade(data: Grade) -> Grade:
    return create_grade(data)

def get_grades():
    return list_grades()
