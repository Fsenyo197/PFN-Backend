from rest_framework import serializers
from blog.models.article_model import Article

class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source="category.name")
    image = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ('category', 'title', 'slug', 'image', 'image_credit', 'body', 'date_published', 'meta_description', 'meta_keywords', 'tags', 'read_time')

    def get_image(self, obj):
        if obj.image:
            # Return only the Cloudinary URL (host URL included)
            return obj.image.url if hasattr(obj.image, 'url') else obj.image
        return None
