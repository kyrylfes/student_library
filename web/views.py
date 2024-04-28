from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from web.models import UserProfile, Material
from web.permissions import IsOwnerOrReadOnly
from web.serializers import MaterialSerializer, UserProfileSerializer


def profile(request):
    profiles = UserProfile.objects.all()
    return render(request, 'profile.html', {'profiles': profiles})


class MaterialViewSet(ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # permission_classes = [IsOwnerOrReadOnly, IsAdminUser]
    filter_fields = ['title', 'owner', 'rating']
    search_fields = ['title', 'owner']
    ordering_fields = ['owner', 'rating']

    def perform_create(self, serializer):
        # serializer.validated_data['owner'] = self.request.user
        serializer.save()


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    # permission_classes = [IsAuthenticated]
