# fastapi_app/auth.py (or apps/users/tokens.py)
import os
import datetime
import jwt
from django.conf import settings
from fastapi import APIRouter

router = APIRouter() 
SECRET = settings.SECRET_KEY
ALGORITHM = "HS256"


def create_access_token(user_id: str, expires_minutes: int = 300):
    now = datetime.datetime.utcnow()
    payload = {
        "user_id": str(user_id),
        "type": "access",
        "exp": now + datetime.timedelta(minutes=expires_minutes),
        "iat": now,
    }
    return jwt.encode(payload, SECRET, algorithm=ALGORITHM)


def create_refresh_token(user_id: str, expires_days: int = 60):
    now = datetime.datetime.utcnow()
    payload = {
        "user_id": str(user_id),
        "type": "refresh",
        "exp": now + datetime.timedelta(days=expires_days),
        "iat": now,
    }
    return jwt.encode(payload, SECRET, algorithm=ALGORITHM)

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token")