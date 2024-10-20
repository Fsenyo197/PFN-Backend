from rest_framework import generics
from blog.api.v1.services.discount_service import DiscountCodeService
from ..serializers.discount_serializers import DiscountCodeSerializer

class DiscountCodeList(generics.ListAPIView):
    """
    API view to list all discount codes.
    """
    serializer_class = DiscountCodeSerializer
    pagination_class = None

    def get_queryset(self):
        service = DiscountCodeService()
        return service.get_all_discount_codes()

class ActiveDiscountCodeList(generics.ListAPIView):
    """
    API view to list only active discount codes.
    """
    serializer_class = DiscountCodeSerializer

    def get_queryset(self):
        service = DiscountCodeService()
        return service.get_active_discount_codes()

class FirmDiscountCodeList(generics.ListAPIView):
    """
    API view to list discount codes by firm name.
    """
    serializer_class = DiscountCodeSerializer

    def get_queryset(self):
        firm_name = self.kwargs['firm_name']
        service = DiscountCodeService()
        return service.get_discount_code_by_firm(firm_name)

class DiscountCodeDetail(generics.RetrieveAPIView):
    """
    API view to retrieve a discount code by its code.
    """
    serializer_class = DiscountCodeSerializer

    def get_object(self):
        code = self.kwargs['code']
        service = DiscountCodeService()
        return service.get_discount_code_by_code(code)
