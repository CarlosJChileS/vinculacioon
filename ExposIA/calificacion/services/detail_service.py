from ..models import GradeDetail
from ..repositories.detail_repo import create_detail, list_details

def add_detail(data: GradeDetail) -> GradeDetail:
    return create_detail(data)

def get_details():
    return list_details()
