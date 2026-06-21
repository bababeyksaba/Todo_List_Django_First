from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/tasks/', views.task_list_api),
    path('api/tasks/<int:pk>/', views.task_detail_api),
]
