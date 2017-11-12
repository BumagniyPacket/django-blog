from django.conf.urls import url

from .views import CommentApproveView, CommentDeleteView

urlpatterns = [
    url(r'^(?P<pk>\d+)/delete$', CommentDeleteView.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/approve$', CommentApproveView.as_view(), name='approve'),
]
