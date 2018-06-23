from rest_framework import serializers

from .models import Article, Tag
from apps.categories.serializers import CategorySerializer


class ArticleListSerializer(serializers.ModelSerializer):
    url = serializers.ReadOnlyField(source='get_absolute_url',)
    image = serializers.ReadOnlyField(source='image.url')

    class Meta:
        model = Article
        fields = ('title', 'url', 'image', 'description', 'timestamp')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ArticleDetailSerializer(serializers.ModelSerializer):
    image = serializers.ReadOnlyField(source='image.url')
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Article
        fields = '__all__'
