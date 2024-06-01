from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookmark_list, name='bookmark_list'),
    path('<int:pk>/', views.bookmark_detail, name='bookmark_detail'),
]
