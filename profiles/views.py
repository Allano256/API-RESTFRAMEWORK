from rest_framework import generics
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer



# from django.http import Http404
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Profile
# from .serializers import ProfileSerializer
# from drf_api.permissions import IsOwnerOrReadOnly

# # Create your views here.
# class ProfileList(APIView):
#     def get(self, request):
#         profiles=Profile.objects.all()
#         serializer = ProfileSerializer(profiles, many=True, context={'request' : request})
#         return Response(serializer.data)
    
# class ProfileDetail(APIView):
#     """
#     Getting a profile/Creating a profile by id
#     """
#     """
#     serializer_class = ProfileSerializer/This helps us to automatically add a form with the fields already stated.
#     """
#     serializer_class = ProfileSerializer
#     """
#     Have the permissions in ana array format.
#     """
#     permission_classes = [IsOwnerOrReadOnly]

#     def get_object(self, pk):
#         try:
#             profile = Profile.objects.get(pk=pk)
#             self.check_object_permissions(self.request, Profile)
#             return profile
#         except Profile.DoesNotExist:
#             raise Http404
        
#     def get(self, request, pk):
#         profile = self.get_object(pk)
#         serializer = ProfileSerializer(profile,context={'request' : request} )
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
   
#     def put(self, request,pk):
#         """
#         Updating a profile/retriev a profile by Id
#         """
#         profile = self.get_object(pk)
#         serializer = ProfileSerializer(profile, data=request.data, context={'request' : request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)