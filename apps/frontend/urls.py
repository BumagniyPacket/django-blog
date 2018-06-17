from django.conf.urls import url

from .views import BlogMainFrontendView

urlpatterns = [
    url(r'^$', BlogMainFrontendView.as_view(), name='list'),
]
