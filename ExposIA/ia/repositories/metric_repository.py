from typing import List, Optional

from ..models.metric import (
    MetricType, Metric, Parameter, MetricTypeOrm, MetricOrm, ParameterOrm
)
from ...common.database import SessionLocal


def _to_pydantic(obj, model):
    return model(**obj.__dict__)


def create_metric_type(data: MetricType) -> MetricType:
    with SessionLocal() as session:
        obj = MetricTypeOrm(**data.model_dump(exclude={"id"}))
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return _to_pydantic(obj, MetricType)


def list_metric_types() -> List[MetricType]:
    with SessionLocal() as session:
        objs = session.query(MetricTypeOrm).all()
        return [_to_pydantic(o, MetricType) for o in objs]


def get_metric_type(obj_id: int) -> Optional[MetricType]:
    with SessionLocal() as session:
        obj = session.get(MetricTypeOrm, obj_id)
        return _to_pydantic(obj, MetricType) if obj else None


def update_metric_type(obj_id: int, data: MetricType) -> Optional[MetricType]:
    with SessionLocal() as session:
        obj = session.get(MetricTypeOrm, obj_id)
        if not obj:
            return None
        for k, v in data.model_dump(exclude={"id"}).items():
            setattr(obj, k, v)
        session.commit()
        return _to_pydantic(obj, MetricType)


def delete_metric_type(obj_id: int) -> bool:
    with SessionLocal() as session:
        obj = session.get(MetricTypeOrm, obj_id)
        if not obj:
            return False
        session.delete(obj)
        session.commit()
        return True


def create_metric(data: Metric) -> Metric:
    with SessionLocal() as session:
        obj = MetricOrm(**data.model_dump(exclude={"id"}))
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return _to_pydantic(obj, Metric)


def list_metrics() -> List[Metric]:
    with SessionLocal() as session:
        objs = session.query(MetricOrm).all()
        return [_to_pydantic(o, Metric) for o in objs]


def get_metric(obj_id: int) -> Optional[Metric]:
    with SessionLocal() as session:
        obj = session.get(MetricOrm, obj_id)
        return _to_pydantic(obj, Metric) if obj else None


def update_metric(obj_id: int, data: Metric) -> Optional[Metric]:
    with SessionLocal() as session:
        obj = session.get(MetricOrm, obj_id)
        if not obj:
            return None
        for k, v in data.model_dump(exclude={"id"}).items():
            setattr(obj, k, v)
        session.commit()
        return _to_pydantic(obj, Metric)


def delete_metric(obj_id: int) -> bool:
    with SessionLocal() as session:
        obj = session.get(MetricOrm, obj_id)
        if not obj:
            return False
        session.delete(obj)
        session.commit()
        return True


def create_parameter(data: Parameter) -> Parameter:
    with SessionLocal() as session:
        obj = ParameterOrm(**data.model_dump(exclude={"id"}))
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return _to_pydantic(obj, Parameter)


def list_parameters() -> List[Parameter]:
    with SessionLocal() as session:
        objs = session.query(ParameterOrm).all()
        return [_to_pydantic(o, Parameter) for o in objs]


def get_parameter(obj_id: int) -> Optional[Parameter]:
    with SessionLocal() as session:
        obj = session.get(ParameterOrm, obj_id)
        return _to_pydantic(obj, Parameter) if obj else None


def update_parameter(obj_id: int, data: Parameter) -> Optional[Parameter]:
    with SessionLocal() as session:
        obj = session.get(ParameterOrm, obj_id)
        if not obj:
            return None
        for k, v in data.model_dump(exclude={"id"}).items():
            setattr(obj, k, v)
        session.commit()
        return _to_pydantic(obj, Parameter)


def delete_parameter(obj_id: int) -> bool:
    with SessionLocal() as session:
        obj = session.get(ParameterOrm, obj_id)
        if not obj:
            return False
        session.delete(obj)
        session.commit()
        return True
