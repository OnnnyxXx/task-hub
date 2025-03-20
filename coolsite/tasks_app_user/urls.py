from django.urls import path, include

from . import views
from .views import *


urlpatterns = [
    path('', views.TaskView.as_view(), name='tasks_home'),
    path('create/', views.CreateTask.as_view(), name='create'),
    path('category/', views.CategoryView.as_view(), name='category'),

    path('<int:pk>', views.TasksDetailView.as_view(), name='details_tasks'),
    path('<int:pk>/update', views.TasksUpdateView.as_view(), name='update_tasks'),
    path('<int:pk>/delete', views.TasksDeleteView.as_view(), name='delete_tasks'),

]
