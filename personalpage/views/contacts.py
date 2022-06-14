from .views import TemplateView
from django.shortcuts import render
from api.models import Social


class ContactsView(TemplateView):
    title = "ajauniskis Contacts"
    template_name = "contacts.html"

    socials = Social.objects.all()

    def get(self, request):
        # updateparams.delay()
        context = {
            "title": "Contacts",
            "socials": self.socials,
        }
        return render(request, self.template_name, context)
