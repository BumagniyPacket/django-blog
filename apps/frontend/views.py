from django.views.generic import DetailView, ListView

from apps.articles.models import Article


class BlogMainFrontendView(ListView):
    template_name = 'frontend/blog_list.html'
    queryset = Article.objects.published()


class BlogDetailFrontendView(DetailView):
    model = Article
    template_name = 'frontend/detail_article.html'
