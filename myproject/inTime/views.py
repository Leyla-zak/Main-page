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

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        if not is_password_strong_enough(password):
            return render(request, 'registration.html', {'error': 'Пожалуйста, введите надежный пароль.'})

        try:
            user = create_user_account(
                data={
                    'name': name,
                    'email': email,
                    'password': hash_password(password)
                },
                session=get_session(),
                background_tasks=None  # или передайте фоновые задачи, если необходимо
            )
            # Дальнейшая обработка успешной регистрации, например, аутентификация пользователя
            return redirect('login')
        except Exception as e:
            return render(request, 'registration.html', {'error': str(e)})

    return render(request, 'registration.html')
