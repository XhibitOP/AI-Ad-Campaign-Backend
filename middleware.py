from fastapi import Header, HTTPException
import jwt
import os
from dotenv import load_dotenv

load_dotenv()

SECRET = os.getenv("SECRET_KEY")


def verify_token(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="No token provided")

    try:
        # Format: "Bearer <token>"
        token = authorization.split(" ")[1]

        payload = jwt.decode(token, SECRET, algorithms=["HS256"])

        return payload  # contains email
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired token")