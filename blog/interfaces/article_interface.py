from abc import ABC, abstractmethod
from typing import List, Optional
from blog.models.article_model import Article

class ArticleRepositoryInterface(ABC):
    @abstractmethod
    def get_all_articles(self) -> List[Article]:
        pass

    @abstractmethod
    def get_article_by_id(self, article_id: int) -> Optional[Article]:
        pass

    @abstractmethod
    def create_article(self, title: str, content: str, author_id: int, category_id: int) -> Article:
        pass

    @abstractmethod
    def update_article(self, article_id: int, title: str, content: str) -> bool:
        pass

    @abstractmethod
    def delete_article(self, article_id: int) -> bool:
        pass
