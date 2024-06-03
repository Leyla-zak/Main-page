
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic.list import ListView
from .models import Task
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.forms import *
from django.contrib.auth import login
from .forms import RegisterForm
from django.core.exceptions import ValidationError
from django import forms
from rest_framework import generics
from .serializers import UserSerializer
from django.contrib.auth.models import User

def index(request):
    return render(request, "index.html")

def logout_view(request):
    logout(request)
    messages.success(request, "Вы успешно вышли из системы.")
    return redirect('/')
  
def calen(request):
    return render(request, "MyCalendar.html")

def validate_date(date):
    try:
        import datetime
        date_obj = datetime.datetime.strptime(date, "%Y-%m-%d")
        if len(str(date_obj.year)) != 4:
            raise ValidationError("The year should have 4 digits.")
    except ValueError:
        raise ValidationError("Invalid date format. Please use YYYY-MM-DD.")



class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer 

class RegisterView(FormView):
    template_name = 'signup.html'
    form_class = RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
            
        return super(RegisterView, self).form_valid(form)
    
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'due_date']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }
        validators = {
            'due_date': [validate_date]
        }
        
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super().form_valid(form)
       
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        messages.success(self.request, "The task was updated successfully.")
        return super().form_valid(form)

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super().form_valid(form)

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
    
def home(request):
    return render(request,'index.html')