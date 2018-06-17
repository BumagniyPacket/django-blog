from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from random import choice

from django.views.generic import DetailView, ListView
from django.views import View
from filer.models import Folder

from apps.articles.models import Article


class BlogMainFrontendView(ListView):
    template_name = 'frontend/blog_list.html'
    queryset = Article.objects.published()


class BlogDetailFrontendView(DetailView):
    model = Article
    template_name = 'frontend/detail_article.html'


class RandomBackgroundFrontendView(View):
    def get(self, *args, **kwargs):
        folder = get_object_or_404(Folder, name='backgrounds')
        images = folder.files
        image = choice(images)
        return HttpResponseRedirect(image.url)
