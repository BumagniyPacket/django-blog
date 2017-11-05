from django.conf.urls import url

from .views import APICommentsList

urlpatterns = [
    url(r'^', APICommentsList.as_view())

]
