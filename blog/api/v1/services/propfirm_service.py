from blog.api.v1.repositories.propfirm_repository import PropFirmRepository

class PropFirmService:
    def __init__(self):
        self.repository = PropFirmRepository()

    def get_all_firms(self):
        return self.repository.get_all()
    