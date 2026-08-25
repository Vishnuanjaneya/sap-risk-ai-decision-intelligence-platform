from fastapi import APIRouter
from typing import List

from schemas.history import PredictionHistory
from services.firebase_service import get_prediction_history

router = APIRouter(
    tags=["History"]
)


@router.get(
    "/history",
    response_model=List[PredictionHistory]
)
def get_history():
    return get_prediction_history()