from fastapi import APIRouter
from fastapi_app.views.user_views import router as user_router

router = APIRouter()

router.include_router(user_router, prefix="/users", tags=["Users"])



