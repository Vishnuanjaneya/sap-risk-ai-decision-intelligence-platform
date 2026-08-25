from fastapi import APIRouter

from schemas.prediction import PredictionRequest

from services.prediction_service import predict_risk
from services.firebase_service import save_prediction

router = APIRouter(
    tags=["Prediction"]
)


@router.post("/predict")
def predict(data: PredictionRequest):

    result = predict_risk(data)

    save_prediction({
        "module": data.module,
        "objects_changed": data.objects_changed,
        "lines_changed": data.lines_changed,
        "conflicts": data.conflicts,
        "history_failures": data.history_failures,
        "transport_stage": data.transport_stage,
        "change_request_status": data.change_request_status,
        "risk": result["risk"],
        "confidence": result["confidence"],
        "decision": result["decision"]
    })

    return result