from pydantic import BaseModel, EmailStr


class SignupSchema(BaseModel):
    email : EmailStr
    password : str
    first_name : str | None = None
    last_name : str | None = None
    role : str | None = "customer"

class LoginSchema(BaseModel):
    email : EmailStr
    password : str

class TokenResponse(BaseModel):
    access_token : str
    refresh_token: str
    token_type : str = "bearer"    