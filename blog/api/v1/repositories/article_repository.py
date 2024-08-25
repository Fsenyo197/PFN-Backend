from blog.models.article_model import Article

class ArticleRepository:
    def get_published_articles(self):
        return Article.objects.filter(status='PUBLISHED', deleted=False)

    def get_published_articles_by_category(self, category_name):
        return Article.objects.filter(category__name=category_name, status='PUBLISHED', deleted=False)
