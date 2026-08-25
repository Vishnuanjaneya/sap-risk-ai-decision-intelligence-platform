from pydantic import BaseModel


class PredictionHistory(BaseModel):
    id: str
    module: str
    objects_changed: int
    lines_changed: int
    conflicts: int
    history_failures: int
    transport_stage: str
    change_request_status: str
    risk: str
    confidence: float
    decision: str