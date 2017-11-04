from django.conf.urls import url

from .views import PostCreate, PostDelete, PostDetail, PostsList, add_comment, post_update

urlpatterns = [
    url(r'^$', PostsList.as_view(), name='list'),
    url(r'^page=(?P<page>\d+)', PostsList.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', PostDetail.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/delete/$', PostDelete.as_view(), name='delete'),
    url(r'^create', PostCreate.as_view(), name='create'),

    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='edit'),
    url(r'^(?P<slug>[\w-]+)/add_comment/$', add_comment),
]
