from typing import List
from blog.models.article_model import Article
from blog.repositories.dashboard_repository import DashboardRepository

class DashboardService:
    def __init__(self, repository: DashboardRepository):
        self.repository = repository

    def get_recent_published_articles(self, limit: int = 5) -> List[Article]:
        return self.repository.get_recent_published_articles(limit)
    
    def get_total_written_articles(self) -> List[Article]:
        return self.repository.get_written_articles()

    def get_total_published_articles(self) -> List[Article]:
        return self.repository.get_published_articles()

    def get_total_drafted_articles(self) -> List[Article]:
        return self.repository.get_drafted_articles()

    def get_total_deleted_articles(self) -> List[Article]:
        return self.repository.get_deleted_articles()
