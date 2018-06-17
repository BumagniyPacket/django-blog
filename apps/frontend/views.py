from django.views.generic import TemplateView, DetailView

from apps.articles.models import Article


class BlogMainFrontendView(TemplateView):
    template_name = 'frontend/blog_list.html'


class BlogDetailFrontendView(DetailView):
    model = Article
    template_name = 'frontend/detail_article.html'
