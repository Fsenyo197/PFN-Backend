from rest_framework import serializers
from blog.models.article_model import Article

class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()  # Safely handling category
    image = serializers.SerializerMethodField()     # Safely handling image

    class Meta:
        model = Article
        fields = ('category', 'title', 'slug', 'image', 'body', 'date_published', 'meta_description', 'meta_keywords')

    def get_category(self, obj):
        try:
            # Safely return category name if it exists, otherwise return None
            if obj.category and obj.category.name:
                return obj.category.name
            return None  # Handle missing category gracefully
        except Exception as e:
            print(f"Error getting category: {e}")
            return None  # Fallback to None if any error occurs

    def get_image(self, obj):
        try:
            if obj.image:
                image_url = obj.image
                print(f"Original image URL: {image_url}")  # Debug output

                # Fix malformed image URLs by applying hardcoded fix
                if "/res" in image_url:
                    index = image_url.index('/res')
                    fixed_url = image_url[:index-3] + ":/" + image_url[index:]
                    print(f"Fixed image URL: {fixed_url}")  # Debug output
                    return fixed_url
                
                return image_url  # Return original image URL if no fix is needed
            return None  # Return None if image is not present
        except Exception as e:
            print(f"Error processing image: {e}")
            return None  # Fallback to None in case of any error
