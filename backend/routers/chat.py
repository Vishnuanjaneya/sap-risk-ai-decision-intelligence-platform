from fastapi import APIRouter

router = APIRouter(
    tags=["AI Copilot"]
)

@router.post("/copilot")
def copilot():

    return {
        "message": "AI Copilot Ready"
    }