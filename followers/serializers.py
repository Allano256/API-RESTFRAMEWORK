from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower

class FollowersSerializer(serializers.ModelSerializer):
    """
    Serializer for the Follower model
    Create method handles the unique constraint on 'owner' and 'followed'
    """

    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model=Follower
        fields = [
            'id','owner','followed','created_at','followed_name'
        ]

    def create(self,validated_data):
        """
        This will prevent the user from following the same post twice.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail':'possible duplicate'
            })


