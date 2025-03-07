from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path('', views.HomeViews.as_view(), name='home'),
    path('about', views.ViewsAbout.as_view(), name='about'),

]