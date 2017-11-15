from django.conf.urls import url

from .views import APICommentDetail, APICommentsList

urlpatterns = [
    url(r'^comments/$', APICommentsList.as_view()),
    url(r'^comments/(?P<pk>[0-9]+)$', APICommentDetail.as_view())
]
