# urlpatterns = [
#     path('', views.index),
#     re_path(r'^about', views.about),
#     re_path(r'^contact', views.contact),
# ]

from django.contrib import admin
from django.urls import path, include
from inTime import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    # path('LogIn.html/', views.login, name='login'),
    path('LogIn.html/SignUp.html/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logged_out'),
    path('accounts/', include('django.contrib.auth.urls')),
]