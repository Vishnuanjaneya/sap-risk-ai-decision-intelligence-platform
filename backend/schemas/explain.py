from pydantic import BaseModel
from typing import List


class ExplainResponse(BaseModel):
    risk: str
    confidence: float
    decision: str
    reasons: List[str]