from fastapi import FastAPI

from routers.predict import router as predict_router
from routers.history import router as history_router
from routers.explain import router as explain_router
from routers.chat import router as chat_router



app = FastAPI(
    title="SAP Risk AI Decision Intelligence API",
    description="Backend services for SAP Risk Decision Intelligence Platform",
    version="1.0.0"
)

app.include_router(
    predict_router,
    prefix="/api",
    tags=["Prediction"]
)

app.include_router(
    history_router,
    prefix="/api",
    tags=["History"]
)

app.include_router(
    explain_router,
    prefix="/api",
    tags=["Explainability"]
)
app.include_router(chat_router)

@app.get("/")
def health_check():
    return {
        "status": "running",
        "project": "SAP Risk AI Decision Intelligence Platform"
    }