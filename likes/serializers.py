from rest_framework import serializers
from .models import Like

class LikesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = [
            'id', 'created_at', 'owner', 'posts'
        ]