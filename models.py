from pydantic import BaseModel, EmailStr
from typing import Optional


# AUTH
class EmailRequest(BaseModel):
    email: EmailStr


class OTPVerifyRequest(BaseModel):
    email: EmailStr
    otp: str


class TokenResponse(BaseModel):
    token: str


# CAMPAIGNS
class CampaignCreate(BaseModel):
    name: str
    budget: Optional[float] = 20.0


class Campaign(BaseModel):
    id: str
    name: str
    status: str
    budget: float
    roas: float
    ctr: float
    cpc: float


# AI
class AIRequest(BaseModel):
    query: str


class AIResponse(BaseModel):
    response: str