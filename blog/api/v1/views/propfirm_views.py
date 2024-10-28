from rest_framework import generics
from rest_framework.response import Response
from blog.api.v1.serializers.propfirm_serializers import PropFirmSerializer
from blog.models.propfirm_model import PropFirm


class PropFirmListView(generics.ListAPIView):
    """List all PropFirms."""
    serializer_class = PropFirmSerializer

    def get(self, request, *args, **kwargs):
        firms = PropFirm.objects.all()
        serializer = self.get_serializer(firms, many=True)
        return Response(serializer.data)


class PropFirmRulesView(generics.ListAPIView):
    """List all PropFirms with their trading rules."""
    def get(self, request, *args, **kwargs):
        rules = PropFirm.objects.values('name', 'news_rule', 'copy_trading', 'two_percent_rule', 'consistency_rule')
        return Response(rules)


class CountryRestrictionsView(generics.ListAPIView):
    """List all PropFirms with their country restrictions."""
    def get(self, request, *args, **kwargs):
        restrictions = PropFirm.objects.values('name', 'countries_prohibited')
        return Response(restrictions)


class TradingPlatformsView(generics.ListAPIView):
    """List all PropFirms with their trading platforms."""
    def get(self, request, *args, **kwargs):
        platforms = PropFirm.objects.values('name', 'trading_platforms')
        return Response(platforms)


class PaymentOptionsView(generics.ListAPIView):
    """List all PropFirms with their payment options."""
    def get(self, request, *args, **kwargs):
        payment_options = PropFirm.objects.values('name', 'payment_options')
        return Response(payment_options)


class YearEstablishedView(generics.ListAPIView):
    """List all PropFirms with their year of establishment."""
    def get(self, request, *args, **kwargs):
        years = PropFirm.objects.values('name', 'year_established')
        return Response(years)


class AccountPlansView(generics.ListAPIView):
    """List all PropFirms with their account plans."""
    def get(self, request, *args, **kwargs):
        account_plans = PropFirm.objects.values('name', 'account_plans')
        return Response(account_plans)
