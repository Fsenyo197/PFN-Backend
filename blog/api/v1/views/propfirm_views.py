from rest_framework import generics
from rest_framework.response import Response
from blog.api.v1.serializers.propfirm_serializers import PropFirmSerializer
from blog.models.propfirm_model import PropFirm
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

class PropFirmListView(generics.ListAPIView):
    """List all PropFirms where status is 'draft' or is_active is False."""
    serializer_class = PropFirmSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        firms = PropFirm.objects.prefetch_related('account_plans').filter(
            Q(status='publish') & Q(is_active=True)
        )
        serializer = self.get_serializer(firms, many=True)
        return Response(serializer.data)
