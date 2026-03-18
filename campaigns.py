from fastapi import APIRouter
from database import campaigns_collection
from models import CampaignCreate, Campaign
import uuid
from middleware import verify_token
from fastapi import Depends

router = APIRouter()


@router.post("/create")
def create_campaign(data: CampaignCreate, user=Depends(verify_token)):
    campaign = {
        "id": str(uuid.uuid4()),
        "name": data.name,
        "status": "Running",
        "budget": data.budget,
        "roas": 0,
        "ctr": 0,
        "cpc": 0
    }

    campaigns_collection.insert_one(campaign)
    return {"message": "Campaign created"}


@router.get("/", response_model=list[Campaign])
def get_campaigns():
    campaigns = list(campaigns_collection.find({}, {"_id": 0}))
    return campaigns


@router.delete("/{campaign_id}")
def delete_campaign(campaign_id: str):
    campaigns_collection.delete_one({"id": campaign_id})
    return {"message": "Deleted"}


@router.put("/toggle/{campaign_id}")
def toggle_campaign(campaign_id: str):
    campaign = campaigns_collection.find_one({"id": campaign_id})

    if not campaign:
        return {"error": "Campaign not found"}

    new_status = "Paused" if campaign["status"] == "Running" else "Running"

    campaigns_collection.update_one(
        {"id": campaign_id},
        {"$set": {"status": new_status}}
    )

    return {"message": "Updated"}