from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *

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

# class RegisterUser(DataMixin, CreateView):
#     form_class = RegisterUserForm
#     template_name = 'inTime/register.html'
#     success_url = reverse_lazy('login')
 
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title="Регистрация")
#         return dict(list(context.items()) + list(c_def.items()))