import joblib
import pandas as pd

MODEL_PATH = "ml/models/catboost_model.pkl"

model = joblib.load(MODEL_PATH)


def explain_prediction(data):

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
    risk = prediction.flatten()[0]

    probabilities = model.predict_proba(df)
    confidence = round(max(probabilities[0]) * 100, 2)

    if risk == "HIGH":
        decision = "HOLD"
    elif risk == "MEDIUM":
        decision = "REVIEW"
    else:
        decision = "APPROVE"

    reasons = []

    if data.conflicts >= 2:
        reasons.append("Multiple transport conflicts detected")

    if data.history_failures >= 2:
        reasons.append("Historical transport failures increase deployment risk")

    if data.transport_stage == "Production":
        reasons.append("Production deployments require stricter risk controls")

    if data.lines_changed > 150:
        reasons.append("Large code modifications increase deployment complexity")

    if data.objects_changed > 5:
        reasons.append("High number of objects modified in transport request")

    if len(reasons) == 0:
        reasons.append("No significant risk indicators identified")

    return {
        "risk": risk,
        "confidence": confidence,
        "decision": decision,
        "reasons": reasons
    }