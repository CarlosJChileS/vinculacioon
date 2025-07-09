from . import analysis_repository
from ..models.metric import MetricType, Metric, Parameter
from ...common.in_memory import InMemoryRepository

metric_types = InMemoryRepository[MetricType]()
metrics = InMemoryRepository[Metric]()
parameters = InMemoryRepository[Parameter]()

# MetricType CRUD
create_metric_type = metric_types.create
list_metric_types = metric_types.list
get_metric_type = metric_types.get
update_metric_type = metric_types.update
delete_metric_type = metric_types.delete

# Metric CRUD
create_metric = metrics.create
list_metrics = metrics.list
get_metric = metrics.get
update_metric = metrics.update
delete_metric = metrics.delete

# Parameter CRUD
create_parameter = parameters.create
list_parameters = parameters.list
get_parameter = parameters.get
update_parameter = parameters.update
delete_parameter = parameters.delete
