from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.views.generic import View

from blog.forms.blog.article_forms import ArticleUpdateForm, ArticleCreateForm
from blog.services.article_service import ArticleService
from blog.repositories.article_repository import ArticleRepository
from blog.models.article_model import Article


# Initialize the ArticleService
article_service = ArticleService(repository=ArticleRepository())


class DashboardHomeView(View):
    template_name = 'dashboard/author/dashboard_home.html'

    def get(self, request, *args, **kwargs):
        articles_list = article_service.get_all_articles()

        total_articles_written = len(articles_list)
        total_articles_published = len([article for article in articles_list if article.status == Article.PUBLISHED and not article.deleted])
        total_articles_views = sum(article.views for article in articles_list)
        total_articles_comments = sum(article.comments.count() for article in articles_list)

        recent_published_articles_list = article_service.get_recent_published_articles(5)

        context = {
            'total_articles_written': total_articles_written,
            'total_articles_published': total_articles_published,
            'total_articles_views': total_articles_views,
            'total_articles_comments': total_articles_comments,
            'recent_published_articles_list': recent_published_articles_list,
        }

        return render(request, self.template_name, context)


class ArticleWriteView(View):
    template_name = 'dashboard/author/article_create_form.html'

    def get(self, request, *args, **kwargs):
        article_create_form = ArticleCreateForm()
        context = {"article_create_form": article_create_form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        article_create_form = ArticleCreateForm(request.POST, request.FILES)
        action = request.POST.get("action")
        article_status = request.POST["status"]

        if action == "SAVE_AS_DRAFT":
            if article_status == Article.PUBLISHED:
                context = {"article_create_form": article_create_form}
                messages.error(request, "You can't save a published article as draft.")
                return render(request, self.template_name, context)

            if article_create_form.is_valid():
                article_service.create_draft_article(article_create_form)
                messages.success(request, "Article drafted successfully.")
                return redirect("blog:drafted_articles")

            context = {"article_create_form": article_create_form}
            messages.error(request, "Please fill required fields")
            return render(request, self.template_name, context)

        if action == "PUBLISH":
            if article_status == Article.DRAFTED:
                context = {"article_create_form": article_create_form}
                messages.error(request, "You can't publish an article marked as draft.")
                return render(request, self.template_name, context)

            if article_create_form.is_valid():
                new_article = article_service.publish_article(article_create_form)
                messages.success(request, "Article published successfully.")
                return redirect("blog:dashboard_article_detail", slug=new_article.slug)

            context = {"article_create_form": article_create_form}
            messages.error(request, "Please fill required fields")
            return render(request, self.template_name, context)


class ArticleUpdateView(View):
    template_name = 'dashboard/author/article_update_form.html'

    def get(self, request, *args, **kwargs):
        old_article = article_service.get_article_by_slug(self.kwargs.get("slug"))
        article_update_form = ArticleUpdateForm(instance=old_article, initial={'tags': old_article.tags.names})
        context = {"article_update_form": article_update_form, "article": old_article}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        old_article = article_service.get_article_by_slug(self.kwargs.get("slug"))
        article_update_form = ArticleUpdateForm(request.POST, request.FILES, instance=old_article)
        action = request.POST.get("action")
        article_status = request.POST["status"]

        if action == "SAVE_AS_DRAFT":
            if article_status == Article.PUBLISHED:
                context = {"article_update_form": article_update_form}
                messages.error(request, "You can't save a published article as draft.")
                return render(request, self.template_name, context)

            if article_update_form.is_valid():
                article_service.update_draft_article(article_update_form, old_article)
                messages.success(request, "Article drafted successfully.")
                return redirect("blog:drafted_articles")

            context = {"article_update_form": article_update_form}
            messages.error(request, "Please fill required fields")
            return render(request, self.template_name, context)

        if action == "PUBLISH":
            if article_status == Article.DRAFTED:
                context = {"article_update_form": article_update_form}
                messages.error(request, "You can't publish an article marked as draft.")
                return render(request, self.template_name, context)

            if article_update_form.is_valid():
                updated_article = article_service.publish_updated_article(article_update_form, old_article)
                messages.success(request, "Article updated successfully.")
                return redirect("blog:dashboard_article_detail", slug=updated_article.slug)

            context = {"article_update_form": article_update_form}
            messages.error(request, "Please fill required fields")
            return render(request, self.template_name, context)


class ArticleDeleteView(View):
    def get(self, *args, **kwargs):
        article_service.delete_article_by_slug(self.kwargs.get("slug"))
        messages.success(request=self.request, message="Article Deleted Successfully")
        return redirect('blog:deleted_articles')


class DashboardArticleDetailView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'dashboard/author/dashboard_article_detail.html'
        context_object = {}

        article = article_service.get_article_by_slug(self.kwargs.get("slug"))

        context_object['article_title'] = article.title
        context_object['article'] = article

        return render(request, template_name, context_object)


class ArticlePublishView(View):
    def get(self, request, *args, **kwargs):
        article_service.publish_article_by_slug(self.kwargs.get('slug'))
        messages.success(request, f"Article Published successfully.")
        return redirect('blog:dashboard_article_detail', slug=self.kwargs.get('slug'))


class AuthorWrittenArticlesView(View):
    def get(self, request):
        template_name = 'dashboard/author/author_written_article_list.html'
        context_object = {}

        written_articles = article_service.get_written_articles_by_author(request.user.id)
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


class AuthorPublishedArticlesView(View):
    def get(self, request):
        template_name = 'dashboard/author/author_published_article_list.html'
        context_object = {}

        published_articles = article_service.get_published_articles_by_author(request.user.id)
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


class AuthorDraftedArticlesView(View):
    def get(self, request):
        template_name = 'dashboard/author/author_drafted_article_list.html'
        context_object = {}

        drafted_articles = article_service.get_drafted_articles_by_author(request.user.id)
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


class AuthorDeletedArticlesView(View):
    def get(self, request):
        template_name = 'dashboard/author/author_deleted_article_list.html'
        context_object = {}

        deleted_articles = article_service.get_deleted_articles_by_author(request.user.id)
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
