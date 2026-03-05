import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_campaign(product, audience, platform, budget):

    prompt = f"""
    Create a marketing campaign.

    Product: {product}
    Audience: {audience}
    Platform: {platform}
    Budget: {budget}

    Generate:
    1. Headline
    2. Ad copy
    3. 5 hashtags
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content