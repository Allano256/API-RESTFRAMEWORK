from rest_framework import serializers
from .models import Comment



class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model
    Adds three extra fields when returning a list of Comment instances
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile')
    profile_image = serializers.ReadOnlyField(source= 'owner.comment.image.url')

    def get_is_owner(self, obj):
        request =self.context['request']
        return request.user == obj.owner
    class Meta:
        model = Comment
        fields = [
            'id','owner','is_owner','profile_id','profile_image','post','created_at','updated_at', 'content'
        ]
    #     read_only_fields = ['owner']
    # def create(self, validated_data):
    #     # Ensure the 'owner' field is set to the current user
    #     request = self.context.get('request')
    #     if request and request.user.is_authenticated:
    #         validated_data['owner'] = request.user
    #     return super().create(validated_data)

   

class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the comment model used in Detail view 
    Post is a read only field so that we dont have to set it on each update
    When editing a Comment, it should always be associated with the same Post.
    Therefore, we should create an additional serializer which automatically references the Post Id which the comment is associated with.
    """
    post = serializers.ReadOnlyField(source='post.id')