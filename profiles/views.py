from django.shortcuts import render
from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from drf_api.permissions import IsOwnerOrReadOnly

# Create your views here.

class ProfileList(generics.ListAPIView):
    def get(self, request):
        queryset = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True, context={"request": request})
        

class ProfileDetail(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()