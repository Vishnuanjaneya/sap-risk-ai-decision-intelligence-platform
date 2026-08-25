from fastapi import APIRouter
from schemas.prediction import PredictionRequest
from services.prediction_service import predict_risk

router = APIRouter(
    tags=["Prediction"]
)


@router.post("/predict")
def predict(data: PredictionRequest):

    return predict_risk(data)