
from typing import List, Optional

from ..models.feedback import FeedbackModel, Feedback
from ...common.database import SessionLocal


def create_feedback(model: FeedbackModel) -> FeedbackModel:
    with SessionLocal() as session:
        obj = Feedback(**model.model_dump(exclude={"id"}))
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return FeedbackModel(**obj.__dict__)


def list_feedback() -> List[FeedbackModel]:
    with SessionLocal() as session:
        objs = session.query(Feedback).all()
        return [FeedbackModel(**o.__dict__) for o in objs]


def get_feedback(obj_id: int) -> Optional[FeedbackModel]:
    with SessionLocal() as session:
        obj = session.get(Feedback, obj_id)
        return FeedbackModel(**obj.__dict__) if obj else None


def update_feedback(obj_id: int, model: FeedbackModel) -> Optional[FeedbackModel]:
    with SessionLocal() as session:
        obj = session.get(Feedback, obj_id)
        if not obj:
            return None
        for field, value in model.model_dump(exclude={"id"}).items():
            setattr(obj, field, value)
        session.commit()
        return FeedbackModel(**obj.__dict__)


def delete_feedback(obj_id: int) -> bool:
    with SessionLocal() as session:
        obj = session.get(Feedback, obj_id)
        if not obj:
            return False
        session.delete(obj)
        session.commit()
        return True
