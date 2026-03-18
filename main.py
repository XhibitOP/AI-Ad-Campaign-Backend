from fastapi import FastAPI
from auth import router as auth_router
from campaigns import router as campaign_router
from ai import router as ai_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(auth_router, prefix="/auth")
app.include_router(campaign_router, prefix="/campaigns")
app.include_router(ai_router, prefix="/ai")


@app.get("/")
def home():
    return {"message": "Backend Running"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later replace with Vercel URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)