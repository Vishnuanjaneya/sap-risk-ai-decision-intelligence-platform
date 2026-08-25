import joblib
import pandas as pd

MODEL_PATH = "ml/models/catboost_model.pkl"

model = joblib.load(MODEL_PATH)

def predict_risk(data):

    df = pd.DataFrame([{
        "module": data.module,
        "objects_changed": data.objects_changed,
        "lines_changed": data.lines_changed,
        "conflicts": data.conflicts,
        "history_failures": data.history_failures,
        "transport_stage": data.transport_stage,
        "change_request_status": data.change_request_status
    }])

    prediction = model.predict(df)

    risk = prediction[0][0]

    probabilities = model.predict_proba(df)
    confidence = round(max(probabilities[0]) * 100, 2)

    if risk == "HIGH":
        decision = "HOLD"
    elif risk == "MEDIUM":
        decision = "REVIEW"
    else:
        decision = "APPROVE"

    return {
        "risk": risk,
        "confidence": confidence,
        "decision": decision
    }