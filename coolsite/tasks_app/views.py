from django.db.models import Avg
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from rest_framework import viewsets
from tasks_app_user.models import Profile
from .serializers import ProfileSerializer


# class TopUsersViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Profile.objects.annotate(avg_rating=Avg('comment__stars')).order_by('-avg_rating')
#     serializer_class = ProfileSerializer

def index(request):
    profiles = Profile.objects.annotate(avg_rating=Avg('comment__stars')).order_by('-avg_rating')
    return render(request, 'tasks_app/index.html', {'profiles': profiles})


def about(reqeust):
    return render(reqeust, 'tasks_app/about.html')
