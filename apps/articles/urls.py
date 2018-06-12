from django.conf.urls import url

from .views import ArticlesListAPIView

urlpatterns = [
    url(r'^$', ArticlesListAPIView.as_view(), name='list'),
]
