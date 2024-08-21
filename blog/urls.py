# Core Django imports.
from django.urls import path

# Blog application imports.
from blog.views.dashboard.category_views import (
    CategoryCreateView,
    CategoryUpdateView,  # Corrected Update View
    CategoryDetailView,
    CategoryDeleteView
)

from blog.views.dashboard.article_views import (
    ArticleWriteView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleDetailView,
    ArticlePublishView,
)

from blog.views.dashboard.dashboard_views import (
    DashboardHomeView,
    TotalWrittenArticlesView,
    TotalPublishedArticlesView,
    TotalDraftedArticlesView,
    TotalDeletedArticlesView,
)


# Specifies the app name for name spacing.
app_name = "blog"

urlpatterns = [

    # CATEGORY URLS #

    # /category/new/
    path(
        route='category/create/',
        view=CategoryCreateView.as_view(),
        name="category_create"
    ),

    # /category/<str:slug>/update/
    path(
        route='category/<str:slug>/update/',
        view=CategoryUpdateView.as_view(),
        name="category_update"
    ),

    # /category/<int:id>/delete/
    path(
        route='category/<int:id>/delete/',
        view=CategoryDeleteView.as_view(),
        name="category_delete"
    ),

    # /category/<int:id>/
    path(
        route='category/<int:id>/',
        view=CategoryDetailView.as_view(),
        name="category_detail"
    ),


    # ARTICLE URLS #

    # /me/article/write/
    path(
        route='me/article/write/',
        view=ArticleWriteView.as_view(),
        name="article_write"
    ),

    # /me/article/<str:slug>/update/
    path(
        route='me/article/<str:slug>/update/',
        view=ArticleUpdateView.as_view(),
        name="article_update"
    ),

    # /me/<str:slug>/
    path(
        route="me/<str:slug>/",
        view=ArticleDetailView.as_view(),
        name='dashboard_article_detail'
    ),

    # /me/article/<str:slug>/delete/
    path(
        route='me/article/<str:slug>/delete/',
        view=ArticleDeleteView.as_view(),
        name="article_delete"
    ),

    # /article/<str:slug>/publish/
    path(
        route="article/<str:slug>/publish/",
        view=ArticlePublishView.as_view(),
        name="publish_article"
    ),


    # DASHBOARD URLS #

    path(
        route="",
        view=DashboardHomeView.as_view(),
        name="dashboard_home"
    ),

    # /me/articles/written/
    path(
        route="me/articles/written/",
        view=TotalWrittenArticlesView.as_view(),
        name="written_articles"
    ),

    # /me/articles/published/
    path(
        route="me/articles/published/",
        view=TotalPublishedArticlesView.as_view(),
        name="published_articles"
    ),

    # /me/articles/drafts/
    path(
        route="me/articles/drafts/",
        view=TotalDraftedArticlesView.as_view(),
        name="drafted_articles"
    ),

    # /me/articles/deleted/
    path(
        route="me/articles/deleted/",
        view=TotalDeletedArticlesView.as_view(),
        name="deleted_articles"
    ),
]
