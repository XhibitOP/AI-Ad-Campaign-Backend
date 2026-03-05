from pydantic import BaseModel

class Campaign(BaseModel):
    product: str
    audience: str
    platform: str
    budget: str