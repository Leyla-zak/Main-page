from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")
def login(request):
    return render(request, "Login.html")
def calen(request):
    return render(request, "MyCalendar.html")
def mypages(request):
    return render(request, "MyPages.html")