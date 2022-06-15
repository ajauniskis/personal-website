from .views import TemplateView
from django.shortcuts import render
from api.models import Social
from django.http import HttpRequest, HttpResponse


class ContactsView(TemplateView):
    title = "ajauniskis Contacts"
    template_name = "contacts.html"

    socials = Social.objects.all()

    def get(self, request: HttpRequest) -> HttpResponse:
        # updateparams.delay()
        context = {
            "title": "Contact Me",
            "socials": self.socials,
        }
        return render(request, self.template_name, context)
