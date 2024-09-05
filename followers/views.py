from django.shortcuts import render
from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from followers.models import Follower
from followers.serializers import FollowersSerializer



# Create your views here.

class FollowerList(generics.ListCreateAPIView):
    permission_classes =[permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FollowersSerializer
    queryset=Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    class FollowerDetail(generics.RetrieveUpdateAPIView):
        permission_classes = [IsOwnerOrReadOnly]
        serializer_class = FollowersSerializer
        queryset = Follower.objects.all()

