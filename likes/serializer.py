from django.db import IntegrityError
from rest_framework import serializers
from .models import Likes

class LikesSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model
    The create method handles the unique constraint on 'owner' and 'post'
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model= Likes
        fields = [
            'id','created_at','owner','post'
        ]

    def create(self,validated_data):
        """
        This will prevent the user from liking the same post twice.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.validationError({
                'detail':'possible duplicate'
            })
      