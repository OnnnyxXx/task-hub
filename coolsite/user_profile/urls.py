from django.urls import path

from . import views
from .views import *


urlpatterns = [
    path('', views.settings_profile, name='profile'),
    path('user/', user_view, name='user_home'),
    path('user/<int:id>/', user_view, name='user_profile'),
    path('user/<int:id>/add_comment/', views.add_comment_view, name='add_comment'),
    path('comment/update/<int:pk>/', CommentUpdateView.as_view(), name='update_comment'),
    path('comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='delete_comment'),
]