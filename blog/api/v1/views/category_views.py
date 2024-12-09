from rest_framework import generics
from blog.api.v1.services.category_service import CategoryService
from ..serializers.category_serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticated

class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        service = CategoryService()
        return service.get_all_categories()
