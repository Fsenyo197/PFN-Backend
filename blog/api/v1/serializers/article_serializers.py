from rest_framework import serializers
from blog.models.article_model import Article

class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source="category.name")
    image = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ('category', 'title', 'slug', 'image', 'body', 'date_published', 'meta_description', 'meta_keywords')

    def get_image(self, obj):
        if obj.image:
            image_url = obj.image
            print(f"Original image URL: {image_url}")  # Debug output

            # Apply hardcoded fix: replace the first 3 characters before '/res' with ':/'
            if "/res" in image_url:
                index = image_url.index('/res')
                fixed_url = image_url[:index-3] + ":/" + image_url[index:]
                print(f"Fixed image URL: {fixed_url}")  # Debug output
                return fixed_url
            
            return image_url  # Return the original image URL if not applicable

        return None
