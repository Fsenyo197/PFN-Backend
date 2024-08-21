from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import  render
from django.views.generic import View
from blog.services.dashboard_service import DashboardService
from blog.repositories.dashboard_repository import DashboardRepository
from blog.models.article_model import Article


# Initialize the DashboardService
dashboard_service = DashboardService(repository=DashboardRepository())


class DashboardHomeView(View):
    template_name = 'dashboard/dashboard/dashboard_home.html'

    def get(self, request, *args, **kwargs):
        articles_list = dashboard_service.get_total_written_articles()  # Fetch all articles

        total_articles_written = len(articles_list)
        total_articles_published = len([article for article in articles_list if article.status == Article.PUBLISHED and not article.deleted])
        total_articles_views = sum(article.views for article in articles_list)

        recent_published_articles_list = dashboard_service.get_recent_published_articles(5)

        context = {
            'total_articles_written': total_articles_written,
            'total_articles_published': total_articles_published,
            'total_articles_views': total_articles_views,
            'recent_published_articles_list': recent_published_articles_list,
        }

        return render(request, self.template_name, context)

    

class TotalWrittenArticlesView(View):
    def get(self, request):
        template_name = 'dashboard/dashboard/total_written_article_list.html'
        context_object = {}

        written_articles = dashboard_service.get_total_written_articles(request)
        total_articles_written = len(written_articles)

        page = request.GET.get('page', 1)
        paginator = Paginator(written_articles, 5)

        try:
            written_articles_list = paginator.page(page)
        except PageNotAnInteger:
            written_articles_list = paginator.page(1)
        except EmptyPage:
            written_articles_list = paginator.page(paginator.num_pages)

        context_object['written_articles_list'] = written_articles_list
        context_object['total_articles_written'] = total_articles_written

        return render(request, template_name, context_object)


class TotalPublishedArticlesView(View):
    def get(self, request):
        template_name = 'dashboard/dashboard/total_published_article_list.html'
        context_object = {}

        published_articles = dashboard_service.get_total_published_articles(request)
        total_articles_published = len(published_articles)

        page = request.GET.get('page', 1)
        paginator = Paginator(published_articles, 5)

        try:
            published_articles_list = paginator.page(page)
        except PageNotAnInteger:
            published_articles_list = paginator.page(1)
        except EmptyPage:
            published_articles_list = paginator.page(paginator.num_pages)

        context_object['published_articles_list'] = published_articles_list
        context_object['total_articles_published'] = total_articles_published

        return render(request, template_name, context_object)


class TotalDraftedArticlesView(View):
    def get(self, request):
        template_name = 'dashboard/dashboard/total_drafted_article_list.html'
        context_object = {}

        drafted_articles = dashboard_service.get_total_drafted_articles(request)
        total_articles_drafted = len(drafted_articles)

        page = request.GET.get('page', 1)
        paginator = Paginator(drafted_articles, 5)

        try:
            drafted_articles_list = paginator.page(page)
        except PageNotAnInteger:
            drafted_articles_list = paginator.page(1)
        except EmptyPage:
            drafted_articles_list = paginator.page(paginator.num_pages)

        context_object['drafted_articles_list'] = drafted_articles_list
        context_object['total_articles_drafted'] = total_articles_drafted

        return render(request, template_name, context_object)


class TotalDeletedArticlesView(View):
    def get(self, request):
        template_name = 'dashboard/dashboard/total_deleted_article_list.html'
        context_object = {}

        deleted_articles = dashboard_service.get_total_deleted_articles(request)
        total_articles_deleted = len(deleted_articles)

        page = request.GET.get('page', 1)
        paginator = Paginator(deleted_articles, 5)

        try:
            deleted_articles_list = paginator.page(page)
        except PageNotAnInteger:
            deleted_articles_list = paginator.page(1)
        except EmptyPage:
            deleted_articles_list = paginator.page(paginator.num_pages)

        context_object['deleted_articles_list'] = deleted_articles_list
        context_object['total_articles_deleted'] = total_articles_deleted

        return render(request, template_name, context_object)
