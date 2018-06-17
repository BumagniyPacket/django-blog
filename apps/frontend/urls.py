from django.conf.urls import url

from .views import (
    BlogMainFrontendView, BlogDetailFrontendView, RandomBackgroundFrontendView,
)

urlpatterns = [
    url(r'^$', BlogMainFrontendView.as_view(), name='list'),
    url(
        r'^article/(?P<pk>\w+)/$', BlogDetailFrontendView.as_view(),
        name='article-detail'
    ),
    url(
        r'^bg/$', RandomBackgroundFrontendView.as_view(),
        name='blog-background'
    ),
]
