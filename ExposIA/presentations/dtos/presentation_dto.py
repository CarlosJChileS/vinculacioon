from pydantic import BaseModel

class PresentationInfo(BaseModel):
    filename: str
    stored_at: str
