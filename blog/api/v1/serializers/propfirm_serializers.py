from rest_framework import serializers
from blog.models.propfirm_model import PropFirm
import json

class PropFirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropFirm
        fields = '__all__'

    def to_representation(self, instance):
        # Get the default representation
        representation = super().to_representation(instance)

        # Deserialize the account_plans if it's a string
        if isinstance(representation['account_plans'], str):
            try:
                # Convert the string to a JSON object
                representation['account_plans'] = json.loads(representation['account_plans'])
            except json.JSONDecodeError:
                # If conversion fails, leave it as it is
                pass

        return representation
