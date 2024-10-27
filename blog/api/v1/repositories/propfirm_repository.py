from blog.models.propfirm_model import PropFirm
from django.core.exceptions import ObjectDoesNotExist

class PropFirmRepository:
    def get_all(self):
        """Get all PropFirm instances."""
        return PropFirm.objects.all()

    def get_by_id(self, firm_id):
        """Get a PropFirm instance by ID."""
        try:
            return PropFirm.objects.get(id=firm_id)
        except ObjectDoesNotExist:
            return None

    def get_by_name(self, name):
        """Get a PropFirm instance by name."""
        try:
            return PropFirm.objects.get(name=name)
        except ObjectDoesNotExist:
            return None

    def get_by_trading_platform(self, platform):
        """Get all PropFirm instances that support the specified trading platform."""
        return PropFirm.objects.filter(trading_platforms=platform)

    def get_by_prohibited_country(self, country, additional_filters=None):
        """Get all PropFirm instances that prohibit the specified country, with optional additional filters."""
        filters = {'countries_prohibited__icontains': country}
        if additional_filters:
            filters.update(additional_filters)
        
        return PropFirm.objects.filter(**filters)
