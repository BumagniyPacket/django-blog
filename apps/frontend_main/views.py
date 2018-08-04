from django.views.generic import TemplateView


class IndexFrontendView(TemplateView):
    template_name = 'frontend_main/index.html'
