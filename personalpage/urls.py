from django.urls import path
from .views.index import IndexView

app_name = "personalpage"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
