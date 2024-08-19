from typing import List, Optional
from blog.models.article_model import Article
from blog.repositories.article_repository import ArticleRepository

class ArticleService:
    def __init__(self, repository: ArticleRepository):
        self.repository = repository

    def get_all_articles(self) -> List[Article]:
        return self.repository.get_all_articles()

    def get_article_by_id(self, article_id: int) -> Optional[Article]:
        return self.repository.get_article_by_id(article_id)

    def create_article(self, title: str, content: str, author_id: int, category_id: int) -> Article:
        return self.repository.create_article(title, content, author_id, category_id)

    def update_article(self, article_id: int, title: str, content: str) -> bool:
        return self.repository.update_article(article_id, title, content)

    def delete_article(self, article_id: int) -> bool:
        return self.repository.delete_article(article_id)
