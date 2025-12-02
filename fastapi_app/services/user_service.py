from django.contrib.auth import get_user_model
from apps.users.models import RefreshToken
from django.utils import timezone
from datetime import datetime, timedelta
from fastapi import HTTPException
from fastapi_app.auth import create_access_token, create_refresh_token 

User = get_user_model()

class UserService:
    @staticmethod
    def signup(data):
        if User.objects.filter(email=data.email).exists():
            raise HTTPException(status_code=400, detail="Email already registered")
        user = User(
            email=data.email,
            first_name=data.first_name or "",
            last_name=data.last_name or "",
            role=data.role,
        )
        user.set_password(data.password)
        user.save() 
        return user
    
    @staticmethod
    def login(data):
        try:
            user = User.objects.get(email=data.email)
        except User.DoesNotExist:
            raise HTTPException(status_code=400, detail="Invalid credentials")
        if not user.check_password(data.password):
            raise HTTPException(status_code=400, detail="Invalid credentials")
        access = create_access_token(user.id)
        refresh = create_refresh_token(user.id)

        expires_at = timezone.now() + timedelta(days=30)

        RefreshToken.objects.create(
            user=user,
            token=refresh,
            expires_at=expires_at
        )
        return {
            "email": user.email,
            "role": user.role,
            "access": access, 
            "refresh": refresh,
            "token_type": "bearer"
            }