import random
import jwt
import datetime
from dotenv import load_dotenv
from fastapi import APIRouter
from database import users_collection
from models import EmailRequest, OTPVerifyRequest, TokenResponse
from fastapi import HTTPException
import os

router = APIRouter()

load_dotenv()

SECRET = os.getenv("SECRET_KEY")


# Generate OTP
def generate_otp():
    return str(random.randint(100000, 999999))


# SEND OTP
@router.post("/send-otp")
def send_otp(data: EmailRequest):
    email = data.email
    otp = generate_otp()

    users_collection.update_one(
        {"email": email},
        {"$set": {"otp": otp}},
        upsert=True
    )

    print("OTP:", otp)  # testing

    return {"message": "OTP sent"}


# VERIFY OTP
@router.post("/verify-otp", response_model=TokenResponse)
def verify_otp(data: OTPVerifyRequest):
    email = data.email
    otp = data.otp

    user = users_collection.find_one({"email": email})

    if not user or user.get("otp") != otp:
        raise HTTPException(status_code=400, detail="Invalid OTP")

    token = jwt.encode({
        "email": email,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1)
    }, SECRET, algorithm="HS256")

    return {"token": token}