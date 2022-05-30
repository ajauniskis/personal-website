from rest_framework import generics
from rest_framework.views import APIView
from ..models import Social
from ..serializers.social_serializer import SocialSerializer


class SocialView(generics.ListAPIView):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer
