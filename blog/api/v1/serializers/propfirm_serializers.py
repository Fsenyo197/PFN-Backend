from rest_framework import serializers
from blog.models.propfirm_model import PropFirm

class PropFirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropFirm
        fields = '__all__'  # or specify the fields you want to include
