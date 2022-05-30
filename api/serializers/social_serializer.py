from rest_framework import serializers
from ..models import Social


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ("id", "social_name", "username", "social_url", "created_at")
