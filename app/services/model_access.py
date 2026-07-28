from app.config.settings import Settings
from pathlib import Path
import pickle
import json
from jsonschema import validate, ValidationError
from app.context.PlatformContext import PlatformContext

class ModelAccessService:
    def __init__(self, settings: Settings):
        self.settings = settings
        self._model_cache = {}  # Cache to store loaded models

    def get_model(self, context:PlatformContext, input_data:dict):
        # Construct the model path based on the settings and input parameters
        model_path = Path(self.settings.paths.models)/f"{context.model_name}_{context.model_version}.pkl"
        model_key=(context.model_name, context.model_version)
        if self._schema_validation(context.model_name, context.model_version, input_data):
            return self._load_model(model_path, model_key)
        else:
            raise ValueError("Input data does not match the required model input-schema.")

# load the model from the specified path and cache it for future use
    def _load_model(self, model_path: Path, model_key:tuple[str, str]):
        # Placeholder for model loading logic
        if model_key in self._model_cache:
            return self._model_cache[model_key]
          
        if model_path.exists():
            with open(model_path, 'rb') as model_file:
                model = pickle.load(model_file)
                self._model_cache[model_key] = model
        else:
            raise FileNotFoundError(f"Model file not found at {model_path}")

        return self._model_cache[model_key]

# validate input data against the model's schema
    def _schema_validation(self, model_name: str, model_version: str, input_data:dict):
        schema_path = Path(self.settings.paths.schemas)/f"{model_name}_{model_version}.json"

        if not schema_path.exists():
            raise FileNotFoundError(f"Schema not found for the model "
                                    f"{model_name}, version {model_version}"
                                    )
        with open(schema_path, 'r') as schema_file:
            schema = json.load(schema_file)

        try:
            validate(instance=input_data, schema=schema)
            return True
        except ValidationError:
            return False

