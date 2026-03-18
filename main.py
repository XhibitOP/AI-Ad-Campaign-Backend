from fastapi import FastAPI
from auth import router as auth_router
from campaigns import router as campaign_router
from ai import router as ai_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth")
app.include_router(campaign_router, prefix="/campaigns")
app.include_router(ai_router, prefix="/ai")


@app.get("/")
def home():
    return {"message": "Backend Running"}