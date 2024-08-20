from typing import List
from blog.models.article_model import Article

class DashboardRepository:
    def get_recent_published_articles(self, limit: int = 5) -> List[Article]:
        return Article.objects.filter(status=Article.PUBLISHED).order_by('-date_published')[:limit]
    
    def get_total_articles_by_status(self, status: str) -> List[Article]:
        return Article.objects.filter(status=status)

    def get_total_written_articles(self) -> List[Article]:
        return self.get_articles_by_status(Article.DRAFTED)

    def get_total_published_articles(self) -> List[Article]:
        return self.get_articles_by_status(Article.PUBLISHED)

    def get_total_drafted_articles(self) -> List[Article]:
        return self.get_articles_by_status(Article.DRAFTED)

    def get_total_deleted_articles(self) -> List[Article]:
        return self.get_articles_by_status(Article.DELETED)
