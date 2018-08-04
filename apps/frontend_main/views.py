from django.views.generic import TemplateView


class IndexFrontendView(TemplateView):
    template_name = 'frontend_main/index.html'


class AboutFrontendView(TemplateView):
    template_name = 'frontend_main/about.html'

