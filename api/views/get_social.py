from rest_framework.views import APIView
from ..serializers.social_serializer import SocialSerializer
from ..models import Social
from rest_framework.response import Response
from rest_framework import status


class GetSocial(APIView):
    serializer_class = SocialSerializer
    lookup_url_kwarg = "social_name"

    def get(self, request, format=None):
        social_name = request.GET.get(self.lookup_url_kwarg)

        if social_name != None:
            social = Social.objects.filter(social_name=social_name)

            if len(social) > 0:
                data = SocialSerializer(social[0]).data
                return Response(data, status=status.HTTP_200_OK)

            return Response(
                {"Social not found": f"Invalid social_name: {social_name}"},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(
            {"Bad Request": "Code paramater not found in request"},
            status=status.HTTP_400_BAD_REQUEST,
        )
