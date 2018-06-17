from django.views.generic import TemplateView, DetailView


class BlogMainFrontendView(TemplateView):
    template_name = 'frontend/blog_list.html'
