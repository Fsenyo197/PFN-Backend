from rest_framework import serializers
from blog.models.propfirm_model import PropFirm, AccountPlan


class AccountPlanSerializer(serializers.ModelSerializer):
    """Serializer for AccountPlan model."""

    class Meta:
        model = AccountPlan
        exclude = ['date_created', 'date_updated', 'status', 'is_available']


class PropFirmSerializer(serializers.ModelSerializer):
    """Serializer for PropFirm model with nested account plans."""
    account_plans = AccountPlanSerializer(many=True, read_only=True)

    class Meta:
        model = PropFirm
        exclude = ['date_published', 'date_created', 'date_updated', 'status', 'is_active']
