from django.conf.urls import url

from .views import (
    IndexFrontendView,
    AboutFrontendView
)


urlpatterns = [
    url(r'^$', IndexFrontendView.as_view(), name='index'),
    url(r'^about/$', AboutFrontendView.as_view(), name='about'),
]
