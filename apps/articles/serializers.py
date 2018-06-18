from rest_framework import serializers

from .models import Article, Category, Tag


class ArticleListSerializer(serializers.ModelSerializer):
    url = serializers.ReadOnlyField(source='get_absolute_url',)
    image = serializers.ReadOnlyField(source='image.url')

    class Meta:
        model = Article
        fields = ('pk', 'title', 'url', 'image', 'description', 'timestamp')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


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
