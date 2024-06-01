"""
ASGI config for myproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.routes.user import auth_router

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

django_application = get_asgi_application()

app = FastAPI()
app.mount("/django", django_application)

# Роутер для авторизации
app.include_router(auth_router, prefix="/auth", tags=["auth"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
