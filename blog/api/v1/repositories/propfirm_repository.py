from blog.models.propfirm_model import PropFirm

class PropFirmRepository:
    def get_all(self):
        """Get all PropFirm instances."""
        return PropFirm.objects.all()
    
    def get_rules(self):
        """Get trading rules for all PropFirm instances."""
        return PropFirm.objects.values('name', 'news_rule', 'copy_trading', 'consistency_rule')
    
    def get_country_restrictions(self):
        """Get country restrictions for all PropFirm instances."""
        return PropFirm.objects.values('name', 'countries_prohibited')
    
    def get_trading_platforms(self):
        """Get trading platforms choices from PropFirm model."""
        return [{'code': choice[0], 'name': choice[1]} for choice in PropFirm.TRADING_PLATFORMS_CHOICES]
    
    def get_payment_options(self):
        """Get payment options for all PropFirm instances."""
        return PropFirm.objects.values('name', 'payment_options')
    
    def get_year_established(self):
        """Get year established for all PropFirm instances."""
        return PropFirm.objects.values('name', 'year_established')
    
    def get_account_plans(self):
        """Get account plans for all PropFirm instances."""
        return PropFirm.objects.values('name', 'account_plans')
