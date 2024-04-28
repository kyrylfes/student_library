from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from web.models import UserProfile, Material
from web.serializers import MaterialSerializer, UserProfileSerializer


def profile(request):
    profiles = UserProfile.objects.all()
    return render(request, 'profile.html', {'profiles': profiles})


class MaterialViewSet(ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['title', 'owner', 'rating']
    search_fields = ['title', 'owner']
    ordering_fields = ['owner', 'rating']


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
