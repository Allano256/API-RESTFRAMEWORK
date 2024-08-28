from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Profile
        fields =[
                'id', 'owner','created_at', 'updated_at', 'name', 'content', 'images'
                 ]

    