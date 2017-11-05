from rest_framework import serializers

from blog.comments.models import Comment


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('post', 'author', 'timestamp', 'text', 'approved')
