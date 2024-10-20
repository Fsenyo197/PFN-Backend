# Core Django Imports
from django.urls import path

# Blog application imports
from blog.api.v1.views.category_views import CategoryList
from blog.api.v1.views.article_views import ArticleList, CategoryArticleList
from blog.api.v1.views.discount_views import DiscountCodeList, ActiveDiscountCodeList, FirmDiscountCodeList, DiscountCodeDetail

urlpatterns = [
    # Category and Article paths
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('articles/', ArticleList.as_view(), name='article-list'),
    path('articles/category/<str:category_name>/', CategoryArticleList.as_view(), name='category-article-list'),

    # Discount code paths
    path('discount-codes/', DiscountCodeList.as_view(), name='discount-code-list'),
    path('discount-codes/active/', ActiveDiscountCodeList.as_view(), name='active-discount-code-list'),
    path('discount-codes/firm/<str:firm_name>/', FirmDiscountCodeList.as_view(), name='firm-discount-code-list'),
    path('discount-codes/<str:code>/', DiscountCodeDetail.as_view(), name='discount-code-detail'),
]
