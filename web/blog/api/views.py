from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from blog.api.serializers import CommentsSerializer
from blog.comments.models import Comment


class APICommentsList(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer


class APICommentDetail(RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
