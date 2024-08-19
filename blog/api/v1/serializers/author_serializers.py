# Third party imports.
from rest_framework import serializers

# Local application imports
from blog.models.author_model import Profile


class AuthorProfile(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'image')
