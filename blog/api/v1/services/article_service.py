from blog.api.v1.repositories.article_repository import ArticleRepository
from rest_framework.exceptions import NotFound

class ArticleService:
    def __init__(self):
        self.repository = ArticleRepository()

    def get_published_articles(self):
        return self.repository.get_published_articles()

    def get_published_articles_by_category(self, category_name):
        articles = self.repository.get_published_articles_by_category(category_name)
        if not articles.exists():
            raise NotFound(f"No articles found for category '{category_name}'")
        return articles

    def get_published_discounts(self):
        # Retrieve articles from the discount category
        discount_articles = self.repository.get_published_articles_by_category('Discount')
        if not discount_articles.exists():
            raise NotFound("No discount articles found")
        return discount_articles
