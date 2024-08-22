from typing import List, Optional
from blog.models.article_model import Article
from blog.repositories.article_repository import ArticleRepository
from django.core.exceptions import ObjectDoesNotExist

class ArticleService:
    def __init__(self, repository: ArticleRepository):
        self.repository = repository

    def get_all_articles(self) -> List[Article]:
        return self.repository.get_all_articles()

    def get_article_by_id(self, article_id: int) -> Optional[Article]:
        try:
            return self.repository.get_article_by_id(article_id)
        except ObjectDoesNotExist:
            # Handle the case where the article is not found
            raise ValueError(f"Article with ID {article_id} does not exist.")

    def create_article(self, title: str, content: str, category_id: int) -> Article:
        if not title or not content:
            raise ValueError("Title and content are required fields.")
        if not self._is_valid_category(category_id):
            raise ValueError("Invalid category ID.")

        return self.repository.create_article(title, content, category_id)

    def update_article(self, article_id: int, title: str, content: str) -> bool:
        if not title or not content:
            raise ValueError("Title and content are required fields.")
        
        try:
            return self.repository.update_article(article_id, title, content)
        except ObjectDoesNotExist:
            # Handle the case where the article is not found
            raise ValueError(f"Article with ID {article_id} does not exist.")

    def delete_article(self, article_id: int) -> bool:
        try:
            return self.repository.delete_article(article_id)
        except ObjectDoesNotExist:
            # Handle the case where the article is not found
            raise ValueError(f"Article with ID {article_id} does not exist.")
