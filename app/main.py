from fastapi import FastAPI
from app.routes import campaigns

app = FastAPI(
    title="AI Ad Campaign Generator",
    version="1.0"
)

app.include_router(campaigns.router)

@app.get("/")
def root():
    return {"message": "AI Ad Campaign Backend Running"}