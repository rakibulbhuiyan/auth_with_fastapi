from fastapi import APIRouter
from fastapi_app.schemas.user_schema import SignupSchema, LoginSchema, TokenResponse
from fastapi_app.services.user_service import UserService

router = APIRouter()


@router.post("/signup")
def signup(data: SignupSchema):
    user = UserService.signup(data)
    return {
            "message": "User signed up successfully",
            "user_id": user.id,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "role": user.role
        }
@router.post("/login")
def login(data: LoginSchema):
    return UserService.login(data)