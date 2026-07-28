import datetime
import json
from app.config.settings import Settings
from pathlib import Path
from app.context.PlatformContext import PlatformContext

class ModelMonitoringService:
    def __init__(self, settings: Settings):
        self.settings = settings

    def monitor_model(self, context:PlatformContext, prediction:str):

        # Log the prediction result along with the request ID and model details
        log_entry = {
            "request_id": context.request_id,
            "model_name": context.model_name,
            "model_version": context.model_version,
            "prediction": prediction,
            "timestamp":datetime.datetime.now().strftime(self.settings.logging.timestamp_format)
        }
        self._log_prediction(log_entry)

    def _log_prediction(self, log_entry: dict):
        monitoring_dir=Path(self.settings.paths.monitoring)
        monitoring_dir.mkdir(parents=True, exist_ok=True)
        monitoring_path = Path(self.settings.paths.monitoring)/\
        f"{log_entry['model_name']}_{log_entry['model_version']}_{log_entry['request_id']}.json"

        try:
            with open(monitoring_path, 'w') as log_file:
                json.dump(log_entry, log_file, indent=5)
        except Exception as e:
            raise Exception(f"Failed to monitor {log_entry['request_id']}: {e}")
