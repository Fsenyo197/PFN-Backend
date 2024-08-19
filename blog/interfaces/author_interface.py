from abc import ABC, abstractmethod
from typing import List, Optional
from blog.models.author_model import Author

class AuthorRepositoryInterface(ABC):
    @abstractmethod
    def get_all_authors(self) -> List[Author]:
        pass

    @abstractmethod
    def get_author_by_id(self, author_id: int) -> Optional[Author]:
        pass

    @abstractmethod
    def create_author(self, name: str, email: str) -> Author:
        pass

    @abstractmethod
    def update_author(self, author_id: int, name: str, email: str) -> bool:
        pass

    @abstractmethod
    def delete_author(self, author_id: int) -> bool:
        pass
