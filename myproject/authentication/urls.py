from django.urls import path

from django.urls import re_path
from .views import RegistrationAPIView

app_name = 'authentication'
urlpatterns = [
    path('users/', RegistrationAPIView.as_view()),
]
