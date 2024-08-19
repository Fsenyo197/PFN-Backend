from typing import List, Optional
from blog.models.author_model import Author
from blog.interfaces.author_interface import AuthorRepositoryInterface

class AuthorRepository(AuthorRepositoryInterface):
    def get_all_authors(self) -> List[Author]:
        return Author.objects.all()

    def get_author_by_id(self, author_id: int) -> Optional[Author]:
        try:
            return Author.objects.get(id=author_id)
        except Author.DoesNotExist:
            return None

    def create_author(self, name: str, email: str) -> Author:
        author = Author(name=name, email=email)
        author.save()
        return author

    def update_author(self, author_id: int, name: str, email: str) -> bool:
        try:
            author = Author.objects.get(id=author_id)
            author.name = name
            author.email = email
            author.save()
            return True
        except Author.DoesNotExist:
            return False

    def delete_author(self, author_id: int) -> bool:
        try:
            author = Author.objects.get(id=author_id)
            author.delete()
            return True
        except Author.DoesNotExist:
            return False
