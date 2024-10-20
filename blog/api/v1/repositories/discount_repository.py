from blog.models.discount_model import DiscountCode
from django.utils import timezone

class DiscountCodeRepository:
    """
    Repository for managing DiscountCode data access.
    """
    
    def get_all_discount_codes(self):
        return DiscountCode.objects.all()

    def get_active_discount_codes(self):
        current_time = timezone.now()
        return DiscountCode.objects.filter(date__lte=current_time, duration__gte=current_time)

    def get_discount_code_by_firm(self, firm_name):
        return DiscountCode.objects.filter(firm_name=firm_name)

    def get_discount_code_by_code(self, code):
        try:
            return DiscountCode.objects.get(discount_code=code)
        except DiscountCode.DoesNotExist:
            return None
