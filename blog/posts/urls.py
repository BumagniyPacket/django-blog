from django.conf.urls import url

from .views import PostsList, add_comment, post_create, post_delete, post_detail, post_update

urlpatterns = [
    url(r'^$', PostsList.as_view(), name='list'),
    url(r'^page=(?P<page>\d+)', PostsList.as_view()),

    url(r'^create', post_create, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='edit'),
    url(r'^(?P<slug>[\w-]+)/add_comment/$', add_comment),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete, name='delete'),
]
