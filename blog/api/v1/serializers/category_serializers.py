# Third party imports.
from rest_framework import serializers

# Local application imports
from blog.models.article_model import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name')


