from django.contrib import admin
from django.urls import path
from myapp.views import task_list
from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', task_list, name='task_list'),
    path('complete/<int:pk>/',views.complete_task,name="complete"),
    path('delete/<int:pk>/',views.delete_task,name="delete"),
    path('update/<int:pk>/', views.update_task, name="update"),

]
