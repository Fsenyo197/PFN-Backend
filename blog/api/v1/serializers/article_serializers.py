from rest_framework import serializers
from blog.models.article_model import Article

class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source="category.name")
    image = serializers.SerializerMethodField()
    discount_details = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = (
            'id', 'category', 'title', 'slug', 'image', 'image_credit', 
            'body', 'date_published', 'meta_description', 
            'meta_keywords', 'read_time', 'discount_details'
        )

    def get_image(self, obj):
        # Return the uploaded image URL if present; otherwise, return the Cloudinary image URL
        if obj.image:
            return obj.image.url if hasattr(obj.image, 'url') else obj.image
        if obj.image_url:
            return obj.image_url
        return None

    def get_discount_details(self, obj):
        # Return discount details if the article belongs to the discount category
        if obj.category.name == 'Discount Codes':
            return {
                'discount_code': obj.discount_code,
                'discount_percentage': obj.discount_percentage,
                'duration': obj.duration,
                'firm_name': obj.firm_name,
                'website_domain': obj.website_domain
            }
        return None
