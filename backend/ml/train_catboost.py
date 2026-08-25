import pandas as pd
import joblib

from catboost import CatBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

# Load dataset
df = pd.read_csv("ml/sap_transport_dataset.csv")

# Features and target
X = df.drop(columns=["transport_id", "risk_level"])
y = df["risk_level"]

# Find categorical columns
cat_features = X.select_dtypes(include=["object"]).columns.tolist()

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train CatBoost
model = CatBoostClassifier(
    iterations=300,
    depth=6,
    learning_rate=0.1,
    loss_function="MultiClass",
    verbose=100
)

model.fit(
    X_train,
    y_train,
    cat_features=cat_features
)

# Predictions
y_pred = model.predict(X_test)

# Metrics
print("\nAccuracy:")
print(accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "ml/models/catboost_model.pkl")

print("\nModel saved successfully!")
print("Location: ml/models/catboost_model.pkl")