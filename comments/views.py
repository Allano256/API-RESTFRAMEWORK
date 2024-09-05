from rest_framework import generics, permissions, filters
from drf_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Comment
from .serializer import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    """
    The List comes with the Get attribute and Create comes with a Post method, so we dont have to write them ourselves.
    
    """
    serializer_class = CommentSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    # def perform_create(self, serializer):
    #     """
    #     We make sure that the comments are associated with a user upon creation.
    #     """
    #     # serializer.save(owner=self.request.user)
    #     serializer.save(post=self.request.data.get('post_id'))

    def perform_create(self, serializer):
        post_id = self.request.data.get('post_id')  # Get post_id from request data
        # Ensure that post_id exists and is valid before creating the comment
        serializer.save(post_id=post_id)

    filter_backends =[
        DjangoFilterBackend
    ]


    filterset_fields=[
       'post'  
    ]
    

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Here we try to ensure that only the owners of the comments can retrieve,edit or destroy a comment.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()