from blog.models.propfirm_model import PropFirm

class PropFirmRepository:
    def get_all(self):
        """Get all PropFirm instances."""
        return PropFirm.objects.all()
