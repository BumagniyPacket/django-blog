from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.api.serializers import CommentsSerializer
from blog.comments.models import Comment


class APICommentsList(APIView):
    """API для работы со списком пользователей."""

    def get(self, request):
        """Доступ к списку пользоватей."""
        customers = Comment.objects.all()
        serializer = CommentsSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Создание пользователя."""
        serializer = CommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)