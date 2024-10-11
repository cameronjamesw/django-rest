from django.shortcuts import render
from rest_framework import permissions, generics
from .models import Follower
from .serializers import FollowerSerializer
from drf_api.permissions import IsOwnerOrReadOnly

# Create your views here.

class FollowerList(generics.ListCreateAPIView):
    serializer_class = FollowerSerializer
    permission_classes = permission.IsAuthenticatedOrReadOnly
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    serializer_class = FollowerSerializer
    permission_classes = IsOwnerOrReadOnly
    queryset = Follower.objects.all()