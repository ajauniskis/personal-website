from django.test import TestCase
from api.models import Social


class SocialModelTest(TestCase):
    def setUp(self) -> None:
        Social.objects.create(social_name="facebook", username="user")

    def test_social_url(self) -> None:
        facebook = Social.objects.get(social_name="facebook")
        expected = "https://facebook.com/" + facebook.username
        actual = facebook.social_url()

        self.assertEqual(expected, actual)
