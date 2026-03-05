from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ai_services import generate_campaign

router = APIRouter()

class CampaignRequest(BaseModel):
    product: str
    audience: str
    platform: str
    budget: str


@router.post("/generate-campaign")
def generate_ad_campaign(request: CampaignRequest):

    result = generate_campaign(
        request.product,
        request.audience,
        request.platform,
        request.budget
    )

    return {
        "campaign": result
    }