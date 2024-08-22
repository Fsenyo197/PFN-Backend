from typing import List, Optional
from blog.models.article_model import Article
from blog.interfaces.article_interface import ArticleRepositoryInterface

class ArticleRepository(ArticleRepositoryInterface):
    def get_all_articles(self) -> List[Article]:
        return Article.objects.all()

    def get_article_by_id(self, article_id: int) -> Optional[Article]:
        try:
            return Article.objects.get(id=article_id)
        except Article.DoesNotExist:
            return None

    def create_article(self, title: str, content: str, category_id: int) -> Article:
        article = Article(title=title, content=content, category_id=category_id)
        article.save()
        return article

    def update_article(self, article_id: int, title: str, content: str) -> bool:
        try:
            article = Article.objects.get(id=article_id)
            article.title = title
            article.content = content
            article.save()
            return True
        except Article.DoesNotExist:
            return False

    def delete_article(self, article_id: int) -> bool:
        try:
            article = Article.objects.get(id=article_id)
            article.delete()
            return True
        except Article.DoesNotExist:
            return False
