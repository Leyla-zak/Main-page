from django.contrib import admin
from django.urls import path, include
from inTime import views
from django.conf import settings
from django.conf.urls.static import static
from inTime.views import (
    TaskList, 
    TaskDetail, 
    TaskCreate, 
    TaskUpdate,
    TaskDelete
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    
    path('MyCalendar.html/', views.calen, name='calen'),
    # path('MyPages.html/', views.mypages, name='mapages'),

    path('LogIn.html/SignUp.html/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logged_out'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('tasks/', TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(),name='task'),
    path('task/create/', TaskCreate.as_view(),name='task-create'),
    path('task/update/<int:pk>/', TaskUpdate.as_view(),name='task-update'),
    path('task/delete/<int:pk>/', TaskDelete.as_view(),name='task-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)