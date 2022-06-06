from django.urls import path
from .views.index import index

app_name = "personalpage"
urlpatterns = [
    path("", index, name="index"),
]
