from django.conf.urls import url

from .views import PostDelete, PostDetail, PostsList, add_comment, post_create, post_update

urlpatterns = [
    url(r'^$', PostsList.as_view(), name='list'),
    url(r'^page=(?P<page>\d+)', PostsList.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', PostDetail.as_view(), name='detail'),

    url(r'^create', post_create, name='create'),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='edit'),
    url(r'^(?P<slug>[\w-]+)/add_comment/$', add_comment),
    url(r'^(?P<slug>[\w-]+)/delete/$', PostDelete.as_view(), name='delete'),
]
