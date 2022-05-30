from django.urls import path
from .views.index import index
from .views.social_view import SocialView

urlpatterns = [
    path("", index),
    path("social", SocialView.as_view()),
]
