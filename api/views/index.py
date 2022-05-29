from django.http import HttpResponse


def index(request):
    return HttpResponse("Api index page")
