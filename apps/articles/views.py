from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Article
from .serializers import ArticleSerializer


class ArticlesListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleRetrieveView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
