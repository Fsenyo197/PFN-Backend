from django.urls import path
from blog.api.v1.views.category_views import CategoryList
from blog.api.v1.views.article_views import ArticleList, CategoryArticleList, DiscountArticleList
from blog.api.v1.views.propfirm_views import PropFirmListView, PropFirmRulesView, CountryRestrictionsView, TradingPlatformsView, PaymentOptionsView, YearEstablishedView, AccountPlansView

urlpatterns = [
    path('propfirms/', PropFirmListView.as_view(), name='propfirm-list'),
    path('propfirms/rules/', PropFirmRulesView.as_view(), name='propfirm-rules'),
    path('propfirms/country-restrictions/', CountryRestrictionsView.as_view(), name='country-restrictions'),
    path('propfirms/trading-platforms/', TradingPlatformsView.as_view(), name='trading-platforms'),
    path('propfirms/payment-options/', PaymentOptionsView.as_view(), name='payment-options'),
    path('propfirms/year-established/', YearEstablishedView.as_view(), name='year-established'),
    path('propfirms/account-plans/', AccountPlansView.as_view(), name='account-plans'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('articles/', ArticleList.as_view(), name='article-list'),
    path('articles/category/<str:category_name>/', CategoryArticleList.as_view(), name='category-article-list'),
    path('articles/discounts/', DiscountArticleList.as_view(), name='discount-article-list'),
]
