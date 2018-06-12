from rest_framework import serializers

from .models import Article


class ArticleListSerializer(serializers.ModelSerializer):
    url = serializers.ReadOnlyField(source='get_absolute_url',)
    image = serializers.ReadOnlyField(source='image.url')

    class Meta:
        model = Article
        fields = ('pk', 'title', 'url', 'image', 'description', 'timestamp')


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
