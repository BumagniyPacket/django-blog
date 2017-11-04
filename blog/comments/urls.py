from django.conf.urls import url

from .views import comment_approve, comment_delete

urlpatterns = [
    url(r'^(?P<pk>\d+)/delete$', comment_delete, name='delete'),
    url(r'^(?P<pk>\d+)/approve$', comment_approve, name='approve'),
]
