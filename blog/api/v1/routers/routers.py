from django.urls import path
from blog.api.v1.views.category_views import CategoryList
from blog.api.v1.views.article_views import ArticleList, CategoryArticleList, DiscountArticleList
from blog.api.v1.views.propfirm_views import PropFirmListView

urlpatterns = [
    path('propfirms/', PropFirmListView.as_view(), name='propfirm-list'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('articles/', ArticleList.as_view(), name='article-list'),
    path('articles/category/<str:category_name>/', CategoryArticleList.as_view(), name='category-article-list'),
    path('articles/discounts/', DiscountArticleList.as_view(), name='discount-article-list'),
]
