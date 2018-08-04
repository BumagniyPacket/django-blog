from django.conf.urls import url

from .views import (
    BlogMainFrontendView,
    BlogDetailFrontendView,
    RandomBackgroundFrontendView,
    BlogAboutFrontendView,
)

urlpatterns = [
    url(r'^$', BlogMainFrontendView.as_view(), name='list'),
    url(
        r'^article/(?P<pk>\w+)/$', BlogDetailFrontendView.as_view(),
        name='blog-article-detail'
    ),
    url(
        r'^about/$', BlogAboutFrontendView.as_view(),
        name='blog-about'
    ),
    url(
        r'^bg/$', RandomBackgroundFrontendView.as_view(),
        name='blog-background'
    ),
]
