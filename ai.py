from fastapi import APIRouter
from database import campaigns_collection
from models import AIRequest, AIResponse
import openai
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

openai.api_key = os.getenv("OPENAI_API_KEY")


@router.post("/strategy", response_model=AIResponse)
def get_strategy(data: AIRequest):
    query = data.query

    campaigns = list(campaigns_collection.find({}, {"_id": 0}))

    prompt = f"""
You are an expert Ad Campaign AI.

User Query:
{query}

Campaign Data:
{campaigns}

Give:
- ROAS improvement suggestions
- Budget optimization
- Best ad format
- Targeting strategy
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return {
        "response": response["choices"][0]["message"]["content"]
    }