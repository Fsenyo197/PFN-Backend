from rest_framework import generics
from blog.api.v1.services.category_service import CategoryService
from ..serializers.category_serializers import CategorySerializer

class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        service = CategoryService()
        return service.get_all_categories()
