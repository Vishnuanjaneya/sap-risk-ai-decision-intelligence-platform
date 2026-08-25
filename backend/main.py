from fastapi import FastAPI
from routers.predict import router as predict_router

app = FastAPI(
    title="SAP Risk AI Decision Intelligence API",
    description="Backend services for SAP Risk Decision Intelligence Platform",
    version="1.0.0"
)

app.include_router(predict_router)


@app.get("/")
def health_check():

    return {
        "status": "running",
        "project": "SAP Risk AI Decision Intelligence Platform"
    }