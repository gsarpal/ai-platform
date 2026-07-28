from dataclasses import dataclass

@dataclass
class PlatformContext:
    model_name:str
    model_version:str
    request_id:str
