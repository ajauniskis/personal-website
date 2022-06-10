from .views import TemplateView


class IndexView(TemplateView):
    title = "ajauniskis page"
    template_name = "index.html"
