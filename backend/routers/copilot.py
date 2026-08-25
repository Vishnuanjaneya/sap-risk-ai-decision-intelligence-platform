from fastapi import APIRouter

from schemas.copilot import CopilotRequest
from services.groq_service import ask_copilot

router = APIRouter(
    tags=["AI Copilot"]
)


@router.post("/copilot")
def copilot(data: CopilotRequest):

    answer = ask_copilot(data.question)

    return {
        "answer": answer
    }