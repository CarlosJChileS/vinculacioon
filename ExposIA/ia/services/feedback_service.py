from ..models.feedback import FeedbackModel
from ..repositories.feedback_repository import (
    create_feedback, list_feedback, get_feedback, update_feedback, delete_feedback
)


def add_feedback(data: FeedbackModel) -> FeedbackModel:
    return create_feedback(data)


def list_all_feedback():
    return list_feedback()
