import logging
from app.config.settings import Settings
from pathlib import Path    
from app.context.PlatformContext import PlatformContext

class LoggingService:
    def __init__(self, settings: Settings):
        self.settings = settings


    def setup_logging(self, context:PlatformContext):
        log_file_path = Path(self.settings.paths.logs) / \
            f"{context.model_name}_{context.model_version}_{context.request_id}.{self.settings.logging.file_extension}"
        
        log_file_path.parent.mkdir(parents=True, exist_ok=True)

        """logging.basicConfig(
            level=self.settings.logging.level.upper()
            format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
            handlers=[logging.FileHandler(log_file_path),
                      logging.StreamHandler()
                      ]
        )"""

        logger = logging.getLogger(f"{context.model_name}_{context.model_version}_{context.request_id}")
        logger.setLevel(self.settings.logging.level.upper())

        file_handler = logging.FileHandler(log_file_path)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        return logger

    