from django.conf.urls import url

from .views import BlogMainFrontendView, BlogDetailFrontendView

urlpatterns = [
    url(r'^$', BlogMainFrontendView.as_view(), name='list'),
    url(
        r'^(?P<pk>\w+)/$', BlogDetailFrontendView.as_view(),
        name='article-detail'
    )
]
