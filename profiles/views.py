from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    posts_count-number of posts a profile owner has created.
    followers_count-number of users folowing a profile.
    following_count-number of profiles a profile owner is following
    anotate allows to get extra query fields
    """
    queryset = Profile.objects.annotate(
       posts_count= Count('owner__post', dinstinct=True),
       followers_count =Count('owner__followed', dinstinct=True),
       following_count=Count('owner__following',dinstinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer

    filter_backends =[
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    
    # We have to set the filter set fiels to filter profiles that are following a profile given its id

    filterset_fields=[
       'owner__following__followed__profile',
       'owner__followed__owner__profile',
    ]



    ordering_fields=[
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at'
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
       posts_count= Count('owner__post', dinstinct=True),
       followers_count =Count('owner__followed', dinstinct=True),
       following_count=Count('owner__following',dinstinct=True)
    ).order_by('-created_at')
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