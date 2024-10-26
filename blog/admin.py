from django.contrib import admin
from django.utils.html import format_html
from blog.models.propfirm_model import PropFirm
from blog.models.article_model import Article
from blog.models.category_model import Category
from blog.forms.dashboard.propfirm_form import PropFirmForm  # Import the PropFirmForm
import json  # Import json module to handle JSON data

@admin.register(PropFirm)
class PropFirmAdmin(admin.ModelAdmin):
    form = PropFirmForm

    list_display = ('name', 'display_trading_platforms', 'news_rule', 'copy_trading', 'consistency_rule', 'crypto_payout_option')
    list_filter = ('news_rule', 'copy_trading', 'consistency_rule', 'crypto_payout_option')
    search_fields = ('name',)
    ordering = ['name']

    fieldsets = (
        (None, {
            'fields': ('name', 'about', 'trading_platforms', 'phase_type')
        }),
        ('Account Plans', {
            'fields': ('account_plans',),
            'description': 'Enter account plan details as JSON',
        }),
        ('Trading Rules', {
            'fields': ('news_rule', 'copy_trading', 'consistency_rule'),
        }),
        ('Payout Options', {
            'fields': ('crypto_payout_option',),
        }),
        ('Restrictions', {
            'fields': ('countries_prohibited',),
        }),
    )

    def display_trading_platforms(self, obj):
        """ Custom display for trading platforms in the list view. """
        return format_html(", ".join(obj.trading_platforms))
    display_trading_platforms.short_description = 'Trading Platforms'

    def save_model(self, request, obj, form, change):
        account_plans = []
        for plan in request.POST.getlist('account_plans'):
            # Assuming plan is passed as JSON
            account_plans.append(json.loads(plan))
        obj.account_plans = account_plans
        super().save_model(request, obj, form, change)

    class Media:
        js = ('blog/utils/propfirm_admin.js',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for Category model.
    """
    list_display = ('name', 'slug', 'approved')
    list_filter = ('approved',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for Article model.
    """
    list_display = (
        'category', 
        'title', 
        'slug', 
        'status', 
        'discount_code', 
        'firm_name', 
        'discount_percentage', 
        'duration'
    )
    list_filter = ('status', 'date_created', 'date_published',)
    search_fields = ('title', 'body',)
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date_published'
    ordering = ['status', '-date_created']

    readonly_fields = ('views', 'count_words', 'read_time', 'date_created', 'date_updated')

    fieldsets = (
        (None, {
            'fields': (
                'category', 'title', 'slug', 'image', 'image_credit', 
                'body', 'status', 'meta_description', 'meta_keywords', 
                'date_published', 'views', 'count_words', 'read_time'
            )
        }),
        ('Discount Information', {
            'fields': (
                'firm_name', 'discount_code', 'discount_percentage', 
                'duration', 'website_domain'
            ),
            'classes': ('collapse',),
        }),
    )
