from django.test import TestCase
from api.models import Social


class SocialModelTest(TestCase):
    def setUp(self):
        Social.objects.create(social_name="domain.com/", username="user")

    def test_social_url(self):
        facebook = Social.objects.get(social_name="domain.com/")
        expected = facebook.social_name + facebook.username
        actual = facebook.social_url()

        self.assertEqual(expected, actual)
