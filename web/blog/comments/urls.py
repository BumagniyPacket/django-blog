from django.conf.urls import url

from .views import CommentAddView, CommentApproveView, CommentDeleteView

urlpatterns = [
    url(r'^(?P<pk>\d+)/delete$', CommentDeleteView.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/approve$', CommentApproveView.as_view(), name='approve'),
    url(r'^add$', CommentAddView.as_view(), name='add'),
]
