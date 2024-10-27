# blog/views.py
from rest_framework import generics
from rest_framework.response import Response
from blog.api.v1.serializers.propfirm_serializers import PropFirmSerializer
from blog.api.v1.services.propfirm_service import PropFirmService

class PropFirmListView(generics.ListAPIView):
    """List all PropFirms."""
    serializer_class = PropFirmSerializer
    service = PropFirmService()

    def get(self, request, *args, **kwargs):
        firms = self.service.get_all_firms()
        serializer = self.get_serializer(firms, many=True)
        return Response(serializer.data)

class PropFirmDetailView(generics.RetrieveAPIView):
    """Retrieve a specific PropFirm by ID."""
    serializer_class = PropFirmSerializer
    service = PropFirmService()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        firm_id = kwargs.get('id')
        firm = self.service.get_firm_by_id(firm_id)
        if firm:
            serializer = self.get_serializer(firm)
            return Response(serializer.data)
        return Response({"error": "PropFirm not found."}, status=404)

class PropFirmByNameView(generics.RetrieveAPIView):
    """Retrieve a specific PropFirm by name."""
    serializer_class = PropFirmSerializer
    service = PropFirmService()
    lookup_field = 'name'

    def get(self, request, *args, **kwargs):
        name = kwargs.get('name')
        firm = self.service.get_firm_by_name(name)
        if firm:
            serializer = self.get_serializer(firm)
            return Response(serializer.data)
        return Response({"error": "PropFirm not found."}, status=404)

class PropFirmByPlatformView(generics.ListAPIView):
    """List PropFirms by trading platform."""
    serializer_class = PropFirmSerializer
    service = PropFirmService()

    def get(self, request, *args, **kwargs):
        platform = self.request.query_params.get('platform')
        firms = self.service.get_firms_by_trading_platform(platform)
        serializer = self.get_serializer(firms, many=True)
        return Response(serializer.data)

class PropFirmByProhibitedCountriesView(generics.ListAPIView):
    """List PropFirms that are prohibited in specified countries with additional filters."""
    serializer_class = PropFirmSerializer
    service = PropFirmService()

    def get(self, request, *args, **kwargs):
        countries = self.request.query_params.getlist('countries')  # Accepts multiple countries
        additional_filters = {}

        if not countries:
            return Response({"error": "No countries provided."}, status=400)

        firms = []
        for country in countries:
            firms += self.service.get_firms_by_prohibited_country(country, additional_filters)

        unique_firms = list({firm.id: firm for firm in firms}.values())  # Remove duplicates based on ID
        serializer = self.get_serializer(unique_firms, many=True)
        return Response(serializer.data)
