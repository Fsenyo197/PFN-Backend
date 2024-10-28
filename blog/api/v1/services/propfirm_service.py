from blog.api.v1.repositories.propfirm_repository import PropFirmRepository

class PropFirmService:
    def __init__(self):
        self.repository = PropFirmRepository()

    def get_all_firms(self):
        return self.repository.get_all()
    
    def get_rules(self):
        return self.repository.get_rules()
    
    def get_country_restrictions(self):
        return self.repository.get_country_restrictions()
    
    def get_trading_platforms(self):
        return self.repository.get_trading_platforms()
    
    def get_payment_options(self):
        return self.repository.get_payment_options()
    
    def get_year_established(self):
        return self.repository.get_year_established()
      
    def get_account_plans(self):
        return self.repository.get_account_plans()
