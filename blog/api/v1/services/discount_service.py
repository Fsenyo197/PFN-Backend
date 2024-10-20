from blog.api.v1.repositories.discount_repository import DiscountCodeRepository
from rest_framework.exceptions import NotFound

class DiscountCodeService:
    """
    Service layer for DiscountCode logic.
    """
    
    def __init__(self):
        self.repository = DiscountCodeRepository()

    def get_all_discount_codes(self):
        return self.repository.get_all_discount_codes()

    def get_active_discount_codes(self):
        active_codes = self.repository.get_active_discount_codes()
        if not active_codes.exists():
            raise NotFound("No active discount codes found")
        return active_codes

    def get_discount_code_by_firm(self, firm_name):
        discount_codes = self.repository.get_discount_code_by_firm(firm_name)
        if not discount_codes.exists():
            raise NotFound(f"No discount codes found for firm '{firm_name}'")
        return discount_codes

    def get_discount_code_by_code(self, code):
        discount_code = self.repository.get_discount_code_by_code(code)
        if not discount_code:
            raise NotFound(f"No discount code found with code '{code}'")
        return discount_code
