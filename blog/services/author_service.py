from typing import List, Optional
from blog.models.author_model import Author
from blog.repositories.author_repository import AuthorRepository

class AuthorService:
    def __init__(self, repository: AuthorRepository):
        self.repository = repository

    def get_all_authors(self) -> List[Author]:
        return self.repository.get_all_authors()

    def get_author_by_id(self, author_id: int) -> Optional[Author]:
        return self.repository.get_author_by_id(author_id)

    def create_author(self, name: str, email: str) -> Author:
        return self.repository.create_author(name, email)

    def update_author(self, author_id: int, name: str, email: str) -> bool:
        return self.repository.update_author(author_id, name, email)

    def delete_author(self, author_id: int) -> bool:
        return self.repository.delete_author(author_id)
