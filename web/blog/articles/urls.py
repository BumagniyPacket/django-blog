from django.conf.urls import url

from .views import ArticleCreateView, ArticleDeleteView, ArticleDetailView, ArticleUpdateView, ArticlesListView

urlpatterns = [
    url(r'^$', ArticlesListView.as_view(), name='list'),
    url(r'^page=(?P<page>\d+)', ArticlesListView.as_view()),
    url(r'^create', ArticleCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)$', ArticleDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit$', ArticleUpdateView.as_view(), name='edit'),
    url(r'^(?P<slug>[\w-]+)/delete$', ArticleDeleteView.as_view(), name='delete'),
]
