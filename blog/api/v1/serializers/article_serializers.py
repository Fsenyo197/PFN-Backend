from rest_framework import serializers
from blog.models.article_model import Article

class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source="category.name")
    image = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ('category', 'title', 'slug', 'image', 'body', 'date_published', 'meta_description', 'meta_keywords')
