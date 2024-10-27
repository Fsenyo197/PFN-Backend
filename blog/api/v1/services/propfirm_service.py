from blog.api.v1.repositories.propfirm_repository import PropFirmRepository

class PropFirmService:
    def __init__(self):
        self.repository = PropFirmRepository()

    def get_all_firms(self):
        return self.repository.get_all()

    def get_firm_by_id(self, firm_id):
        return self.repository.get_by_id(firm_id)

    def get_firm_by_name(self, name):
        return self.repository.get_by_name(name)

    def get_firms_by_trading_platform(self, platform):
        return self.repository.get_by_trading_platform(platform)

    def get_firms_by_prohibited_country(self, country, additional_filters=None):
        """Get all PropFirm instances that prohibit the specified country with optional additional filters."""
        return self.repository.get_by_prohibited_country(country, additional_filters)
