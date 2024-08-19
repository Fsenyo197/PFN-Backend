from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.views.generic import View

from blog.forms.blog.article_forms import ArticleUpdateForm, ArticleCreateForm
from blog.models.article_models import Article


class DashboardHomeView(View):
    template_name = 'dashboard/author/dashboard_home.html'

    def get(self, request, *args, **kwargs):
        articles_list = Article.objects.all()  # No longer filtered by author

        total_articles_written = len(articles_list)
        total_articles_published = len(articles_list.filter(status=Article.PUBLISHED, deleted=False))
        total_articles_views = sum(article.views for article in articles_list)
        total_articles_comments = sum(article.comments.count() for article in articles_list)

        recent_published_articles_list = articles_list.filter(
            status=Article.PUBLISHED, deleted=False).order_by("-date_published")[:5]

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
                new_article = article_create_form.save(commit=False)
                new_article.date_published = None
                new_article.save()
                article_create_form.save_m2m()

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
                new_article = article_create_form.save(commit=False)
                new_article.save()
                article_create_form.save_m2m()

                messages.success(request, "Article published successfully.")
                return redirect("blog:dashboard_article_detail", slug=new_article.slug)

            context = {"article_create_form": article_create_form}
            messages.error(request, "Please fill required fields")
            return render(request, self.template_name, context)


class ArticleUpdateView(View):
    template_name = 'dashboard/author/article_update_form.html'

    def get(self, request, *args, **kwargs):
        old_article = get_object_or_404(Article, slug=self.kwargs.get("slug"))
        article_update_form = ArticleUpdateForm(instance=old_article, initial={'tags': old_article.tags.names})
        context = {"article_update_form": article_update_form, "article": old_article}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        old_article = get_object_or_404(Article, slug=self.kwargs.get("slug"))
        article_update_form = ArticleUpdateForm(request.POST, request.FILES, instance=old_article)
        action = request.POST.get("action")
        article_status = request.POST["status"]

        if action == "SAVE_AS_DRAFT":
            if article_status == Article.PUBLISHED:
                context = {"article_update_form": article_update_form}
                messages.error(request, "You can't save a published article as draft.")
                return render(request, self.template_name, context)

            if article_update_form.is_valid():
                updated_article = article_update_form.save(commit=False)
                updated_article.date_published = None
                updated_article.date_updated = timezone.now()
                updated_article.save()
                article_update_form.save_m2m()

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
                updated_article = article_update_form.save(commit=False)
                updated_article.date_published = timezone.now()
                updated_article.date_updated = timezone.now()
                updated_article.save()
                article_update_form.save_m2m()

                messages.success(request, "Article updated successfully.")
                return redirect("blog:dashboard_article_detail", slug=updated_article.slug)

            context = {"article_update_form": article_update_form}
            messages.error(request, "Please fill required fields")
            return render(request, self.template_name, context)


class ArticleDeleteView(View):
    def get(self, *args, **kwargs):
        article = get_object_or_404(Article, slug=self.kwargs.get("slug"))
        article.deleted = True
        article.save()
        messages.success(request=self.request, message="Article Deleted Successfully")
        return redirect('blog:deleted_articles')


class DashboardArticleDetailView( View):
    """
       Displays article details.
    """

    def get(self, request, *args, **kwargs):
        """
           Returns article details.
        """
        template_name = 'dashboard/author/dashboard_article_detail.html'
        context_object = {}

        article = get_object_or_404(Article, slug=self.kwargs.get("slug"))

        context_object['article_title'] = article.title
        context_object['article'] = article

        return render(request, template_name, context_object)


class ArticlePublishView( View):
    """
       View to publish a drafted article
    """

    def get(self, request, *args, **kwargs):
        """
            Gets article slug from user and gets the article from the
            database.
            It then sets the status to publish and date published to now and
            then save the article and redirects the author to his/her published
            articles.
        """
        article = get_object_or_404(Article, slug=self.kwargs.get('slug'))
        article.status = Article.PUBLISHED
        article.date_published = timezone.now()
        article.date_updated = timezone.now()
        article.save()

        messages.success(request, f"Article Published successfully.")
        return redirect('blog:dashboard_article_detail', slug=article.slug)


class AuthorWrittenArticlesView( View):
    """
       Displays all articles written by an author.
    """

    def get(self, request):
        """
           Returns all articles written by an author.
        """
        template_name = 'dashboard/author/author_written_article_list.html'
        context_object = {}

        written_articles = Article.objects.filter(author=request.user.id, deleted=False).order_by('-date_created')
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


class AuthorPublishedArticlesView( View):
    """
       Displays published articles by an author.
    """

    def get(self, request):
        """
           Returns published articles by an author.
        """
        template_name = 'dashboard/author/author_published_article_list.html'
        context_object = {}

        published_articles = Article.objects.filter(author=request.user.id,
                                                    status=Article.PUBLISHED, deleted=False).order_by('-date_published')
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


class AuthorDraftedArticlesView( View):
    """
       Displays drafted articles by an author.
    """

    def get(self, request):
        """
           Returns drafted articles by an author.
        """
        template_name = 'dashboard/author/author_drafted_article_list.html'
        context_object = {}

        drafted_articles = Article.objects.filter(author=request.user.id,
                                                  status=Article.DRAFTED, deleted=False).order_by('-date_created')
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


class AuthorDeletedArticlesView( View):
    """
       Displays deleted articles by an author.
    """

    def get(self, request):
        """
           Returns deleted articles by an author.
        """
        template_name = 'dashboard/author/author_deleted_article_list.html'
        context_object = {}

        deleted_articles = Article.objects.filter(author=request.user.id,
                                                  deleted=True).order_by('-date_published')
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
