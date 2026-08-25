import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase only once
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase/firebase-key.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()


def save_prediction(data):
    """
    Save prediction record to Firestore
    """
    doc_ref = db.collection("prediction_history").add(data)

    return {
        "message": "Prediction saved successfully"
    }


def get_prediction_history():
    """
    Retrieve prediction history
    """

    docs = db.collection("prediction_history").stream()

    history = []

    for doc in docs:
        record = doc.to_dict()
        record["id"] = doc.id
        history.append(record)

    return history