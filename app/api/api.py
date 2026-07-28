from fastapi import FastAPI, Request
from pydantic import BaseModel
import uuid
from app.context.PlatformContext import PlatformContext

class PayloadValidation(BaseModel):
    model_name:str
    model_version:str
    input_data:dict

app = FastAPI()

# Check for API health
@app.get("/health")
def health():
    return{"status":"healthy"}

@app.post("/predict")
def predict(payload: PayloadValidation, request:Request):

    context=PlatformContext(
        request_id = str(uuid.uuid4()),
        model_name=payload.model_name,
        model_version=payload.model_version        
    )
    

    logging_service=request.app.state.logging_service
    logger=logging_service.setup_logging(context)

    logger.info(
    f"Prediction request received for model "
    f"{context.model_name} version {context.model_version}"
    )

    serving_service=request.app.state.model_serving
    prediction = serving_service.serve_model(
        context,
        payload.input_data,
    )

    logger.info(f"Model {context.model_name} version {context.model_version} prediction completed")
  
    monitoring_service=request.app.state.monitoring_service
    monitoring_service.monitor_model(
            context,
            prediction)

  
    return {
        "request_id": context.request_id,
        "prediction": prediction,
    }



