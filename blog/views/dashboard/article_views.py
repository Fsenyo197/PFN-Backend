from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import View

from blog.forms.dashboard.article_forms import ArticleUpdateForm, ArticleCreateForm
from blog.services.article_service import ArticleService
from blog.repositories.article_repository import ArticleRepository
from blog.models.article_model import Article


# Initialize the ArticleService
article_service = ArticleService(repository=ArticleRepository())


class ArticleWriteView(View):
    template_name = 'dashboard/article/article_create_form.html'

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
                return redirect("blog:article_detail", slug=new_article.slug)

            context = {"article_create_form": article_create_form}
            messages.error(request, "Please fill required fields")
            return render(request, self.template_name, context)


class ArticleUpdateView(View):
    template_name = 'dashboard/article/article_update_form.html'

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
                return redirect("blog:article_detail", slug=updated_article.slug)

            context = {"article_update_form": article_update_form}
            messages.error(request, "Please fill required fields")
            return render(request, self.template_name, context)


class ArticleDetailView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'dashboard/article/article_detail.html'
        context_object = {}

        article = article_service.get_article_by_slug(self.kwargs.get("slug"))

        context_object['article_title'] = article.title
        context_object['article'] = article

        return render(request, template_name, context_object)


class ArticleDeleteView(View):
    def get(self, *args, **kwargs):
        article_service.delete_article_by_slug(self.kwargs.get("slug"))
        messages.success(request=self.request, message="Article Deleted Successfully")
        return redirect('blog:delete_article')


class ArticlePublishView(View):
    def get(self, request, *args, **kwargs):
        article_service.publish_article_by_slug(self.kwargs.get('slug'))
        messages.success(request, f"Article Published successfully.")
        return redirect('blog:article_detail', slug=self.kwargs.get('slug'))


class ArticleListView(View):
    template_name = 'dashboard/article/article_list.html'

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        context = {
            'articles': articles
        }
        return render(request, self.template_name, context)