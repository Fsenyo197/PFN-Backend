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
