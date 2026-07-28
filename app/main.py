from app.services.model_serving import ModelServingService
from app.services.model_access import ModelAccessService
from app.services.model_monitoring import ModelMonitoringService
from app.services.logging import LoggingService
from app.config.settings import settings
from app.api.api import app

# Objects defined
model_access=ModelAccessService(settings)
model_serving=ModelServingService(model_access)
model_monitoring=ModelMonitoringService(settings)
model_logging=LoggingService(settings)

# Add services to fastAPI application state

app.state.model_serving=model_serving
app.state.monitoring_service=model_monitoring
app.state.logging_service=model_logging


