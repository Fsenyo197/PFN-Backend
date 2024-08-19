from abc import ABC, abstractmethod
from typing import Optional
from blog.models.category_model import Category

class CategoryRepositoryInterface(ABC):
    @abstractmethod
    def get_all_categories(self) -> list[Category]:
        pass

    @abstractmethod
    def get_category_by_id(self, category_id: int) -> Optional[Category]:
        pass

    @abstractmethod
    def create_category(self, name: str) -> Category:
        pass

    @abstractmethod
    def update_category(self, category_id: int, name: str) -> bool:
        pass

    @abstractmethod
    def delete_category(self, category_id: int) -> bool:
        pass

