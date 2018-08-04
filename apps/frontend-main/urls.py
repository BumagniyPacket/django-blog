from django.conf.urls import url

from .views import IndexFrontendView


urlpatterns = [
    url(r'^$', IndexFrontendView.as_view(), name='index'),
]
