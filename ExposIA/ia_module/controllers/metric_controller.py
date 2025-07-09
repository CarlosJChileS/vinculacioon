from fastapi import APIRouter
from ..dtos.metric_dto import MetricDTO, MetricTypeDTO, ParameterDTO
from ..services.metric_service import (
    add_metric_type, get_metric_types, add_metric, get_metrics, add_parameter, get_parameters
)

router = APIRouter(prefix="/metric")

@router.post("/types", response_model=MetricTypeDTO)
async def create_type(data: MetricTypeDTO):
    return add_metric_type(data)

@router.get("/types", response_model=list[MetricTypeDTO])
async def list_types():
    return get_metric_types()

@router.post("/", response_model=MetricDTO)
async def create_metric(data: MetricDTO):
    return add_metric(data)

@router.get("/", response_model=list[MetricDTO])
async def list_metrics_route():
    return get_metrics()

@router.post("/parameters", response_model=ParameterDTO)
async def create_parameter(data: ParameterDTO):
    return add_parameter(data)

@router.get("/parameters", response_model=list[ParameterDTO])
async def list_parameters_route():
    return get_parameters()
