from typing import List, Optional
from blog.models.category_model import Category
from blog.interfaces.category_interface import CategoryRepositoryInterface

class CategoryRepository(CategoryRepositoryInterface):
    def get_all_categories(self) -> List[Category]:
        return Category.objects.all()

    def get_category_by_id(self, category_id: int) -> Optional[Category]:
        try:
            return Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return None

    def create_category(self, name: str) -> Category:
        category = Category(name=name)
        category.save()
        return category

    def update_category(self, category_id: int, name: str) -> bool:
        try:
            category = Category.objects.get(id=category_id)
            category.name = name
            category.save()
            return True
        except Category.DoesNotExist:
            return False

    def delete_category(self, category_id: int) -> bool:
        try:
            category = Category.objects.get(id=category_id)
            category.delete()
            return True
        except Category.DoesNotExist:
            return False
