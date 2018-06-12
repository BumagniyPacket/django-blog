from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Article
from .serializers import ArticleDetailSerializer, ArticleListSerializer


class ArticlesListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer


class ArticleRetrieveView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
