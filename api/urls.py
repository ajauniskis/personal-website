from django.urls import path
from .views.index import index
from .views.social_view import SocialView
from .views.get_social import GetSocial

urlpatterns = [
    path("", index),
    path("social", SocialView.as_view()),
    path("get-social", GetSocial.as_view()),
]
