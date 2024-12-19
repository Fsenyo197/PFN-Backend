from rest_framework import generics
from rest_framework.response import Response
from blog.api.v1.serializers.propfirm_serializers import PropFirmSerializer
from blog.models.propfirm_model import PropFirm
from rest_framework.permissions import IsAuthenticated


class PropFirmListView(generics.ListAPIView):
    """List all PropFirms."""
    serializer_class = PropFirmSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        firms = PropFirm.objects.all()
        serializer = self.get_serializer(firms, many=True)
        return Response(serializer.data)