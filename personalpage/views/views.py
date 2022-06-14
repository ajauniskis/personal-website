from django.views.generic import TemplateView as tw


class TemplateView(tw):
    title = ""

    def get_title(self) -> str:
        return self.title

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_title()
        return context
