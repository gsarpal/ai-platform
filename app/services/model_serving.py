from app.services.model_access import ModelAccessService
from app.context.PlatformContext import PlatformContext

class ModelServingService:
    def __init__(self, model_access_service: ModelAccessService):
        self.model_access_service = model_access_service

    def serve_model(self, context:PlatformContext, input_data:dict):
        
        # Load the model using the model name and version
        model = self.model_access_service.get_model(context, input_data)

        if model:
            return self._model_predict(model, input_data)
        else:
            raise Exception("Model Not Found")

    def _prepare_model_input(self, input_data):
        model_input=[list(input_data.values())]
        return model_input

    def _model_predict(self, model, input_data):
        model_curated_input = self._prepare_model_input(input_data)
        prediction = model.predict(model_curated_input)
        return prediction.tolist()


