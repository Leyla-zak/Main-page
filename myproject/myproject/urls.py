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
    TaskDelete,
    RegisterView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'home'),
    
    path('MyCalendar.html/', views.calen, name='calen'),

    path('logout/', views.logout_view, name='logged_out'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('user/registration/', RegisterView.as_view(),name='signup'),
    path('tasks/', TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(),name='task'),
    path('task/create/', TaskCreate.as_view(),name='task-create'),
    path('task/update/<int:pk>/', TaskUpdate.as_view(),name='task-update'),
    path('task/delete/<int:pk>/', TaskDelete.as_view(),name='task-delete'),

    path('api/', include('inTime.urls')), 
    path('api-auth/', include('rest_framework.urls')),  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)