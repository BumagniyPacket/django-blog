from django.conf.urls import url

from .views import (
    ArticleCategoryListAPIView,
)

urlpatterns = [
    url(r'^$', ArticleCategoryListAPIView.as_view(), name='category-list'),
]
