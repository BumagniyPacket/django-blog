from django.conf.urls import url

from .views import (
    post_create,
    post_delete,
    post_detail,
    post_list,
    post_update,
    add_comment,
)

urlpatterns = [
    url(r'^$', post_list, name='list'),
    url(r'^create', post_create, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='edit'),
    url(r'^(?P<slug>[\w-]+)/add_comment/$', add_comment),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete, name='delete'),
]
