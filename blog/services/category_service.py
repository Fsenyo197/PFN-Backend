from typing import List, Optional
from blog.models.category_model import Category
from blog.repositories.category_repository import CategoryRepository

class CategoryService:
    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    def get_all_categories(self) -> List[Category]:
        return self.repository.get_all_categories()

    def get_category_by_id(self, category_id: int) -> Optional[Category]:
        return self.repository.get_category_by_id(category_id)

    def create_category(self, name: str) -> Category:
        return self.repository.create_category(name)

    def update_category(self, category_id: int, name: str) -> bool:
        return self.repository.update_category(category_id, name)

    def delete_category(self, category_id: int) -> bool:
        return self.repository.delete_category(category_id)
