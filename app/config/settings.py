from dataclasses import dataclass
import yaml
from pathlib import Path

# Define dataclasses for structured configuration
@dataclass
class AppConfig:
    name: str
    version: str
    environment: str

@dataclass
class ServerConfig:
    host: str
    port: int
    workers: int

@dataclass
class LoggingConfig:
    level: str
    timestamp_format: str
    filename: str
    file_extension: str

@dataclass
class PathsConfig:
    models: str
    logs: str
    schemas: str
    monitoring: str


@dataclass
class Settings:
    app: AppConfig
    server: ServerConfig
    logging: LoggingConfig
    paths: PathsConfig



# Read settings from YAML file
config_file = Path(__file__).parent / "application.yml"

with open(config_file, 'r') as file:
    config_data = yaml.safe_load(file)

# Objects to hold the configuration data

app_config = AppConfig(**config_data['app'])
server_config = ServerConfig(**config_data['server'])
logging_config = LoggingConfig(**config_data['logging'])
paths_config = PathsConfig(**config_data['paths'])

settings = Settings(
    app=app_config,
    server=server_config,
    logging=logging_config,
    paths=paths_config
)









