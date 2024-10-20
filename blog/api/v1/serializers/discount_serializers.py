from rest_framework import serializers
from blog.models.discount_model import DiscountCode

class DiscountCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountCode
        fields = ('firm_name', 'discount_code', 'discount_percentage', 'title', 'image', 'body', 'date', 'duration')
