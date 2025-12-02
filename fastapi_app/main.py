# fastapi_app/main.py
import os
import django
from fastapi import FastAPI

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "auth_project.settings")
django.setup()

from fastapi_app.router import router

app = FastAPI()
app.include_router(router, prefix="/api")
