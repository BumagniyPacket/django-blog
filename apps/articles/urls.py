from django.conf.urls import url

from .views import ArticlesListAPIView, ArticleRetrieveView

urlpatterns = [
    url(r'^$', ArticlesListAPIView.as_view(), name='list'),
    url(
        r'^(?P<pk>\w+)/$',
        ArticleRetrieveView.as_view(), name='article-detail'
    ),
]
