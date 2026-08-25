from pydantic import BaseModel

class PredictionRequest(BaseModel):
    module: str
    objects_changed: int
    lines_changed: int
    conflicts: int
    history_failures: int
    transport_stage: str
    change_request_status: str