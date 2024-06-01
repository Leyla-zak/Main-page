from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from app.models.user import User
from app.config.security import hash_password, verify_password, is_password_strong_enough
from app.config.database import get_session
from app.services.user import create_user_account

def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "Login.html")

def signup(request):
    return render(request, "SignUp.html")

def calen(request):
    return render(request, "MyCalendar.html")

def mypages(request):
    return render(request, "MyPages.html")