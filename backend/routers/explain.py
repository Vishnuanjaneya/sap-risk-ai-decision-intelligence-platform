from fastapi import APIRouter

from schemas.prediction import PredictionRequest
from services.explanation_service import explain_prediction

router = APIRouter(
    tags=["Explainability"]
)


@router.post("/explain")
def explain(data: PredictionRequest):
    return explain_prediction(data)