from rest_framework import generics
from blog.api.v1.services.article_service import ArticleService
from ..serializers.article_serializers import ArticleSerializer
from rest_framework.permissions import IsAuthenticated

class ArticleList(generics.ListAPIView):
    serializer_class = ArticleSerializer
    pagination_class = None
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        service = ArticleService()
        return service.get_published_articles()

class CategoryArticleList(generics.ListAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        service = ArticleService()
        return service.get_published_articles_by_category(category_name)

class DiscountArticleList(generics.ListAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        service = ArticleService()
        return service.get_published_discounts()