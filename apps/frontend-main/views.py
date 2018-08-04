from django.views.generic import TemplateView


class IndexFrontendView(TemplateView):
    template_name = 'frontend/index.html'
