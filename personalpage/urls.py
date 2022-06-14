from django.urls import path
from .views.index import IndexView
from .views.contacts import ContactsView

app_name = "personalpage"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("contacts", ContactsView.as_view(), name="contacts"),
]
