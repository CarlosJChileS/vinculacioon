from ..models.metric import MetricType, Metric, Parameter
from ..repositories.metric_repository import (
    create_metric_type, list_metric_types, get_metric_type, update_metric_type, delete_metric_type,
    create_metric, list_metrics, get_metric, update_metric, delete_metric,
    create_parameter, list_parameters, get_parameter, update_parameter, delete_parameter,
)

# simple passthrough services

def add_metric_type(data: MetricType) -> MetricType:
    return create_metric_type(data)

def get_metric_types():
    return list_metric_types()

def add_metric(data: Metric) -> Metric:
    return create_metric(data)

def get_metrics():
    return list_metrics()

def add_parameter(data: Parameter) -> Parameter:
    return create_parameter(data)

def get_parameters():
    return list_parameters()
