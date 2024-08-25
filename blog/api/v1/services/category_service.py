from blog.api.v1.repositories.category_repository import CategoryRepository

class CategoryService:
    def __init__(self):
        self.repository = CategoryRepository()

    def get_all_categories(self):
        return self.repository.get_all_categories()
