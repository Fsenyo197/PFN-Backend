from django.contrib import admin
from django.utils.html import format_html
from blog.models.propfirm_model import PropFirm
from blog.models.article_model import Article
from blog.models.category_model import Category
from blog.forms.dashboard.propfirm_form import PropFirmForm
import json

@admin.register(PropFirm)
class PropFirmAdmin(admin.ModelAdmin):
    form = PropFirmForm

    fieldsets = (
        (None, {
            'fields': ('name', 'about', 'trading_platforms')
        }),
        ('Account Plans', {
            'fields': ('account_plans',),
            'description': format_html(
                '<div id="account-plans-container"></div>'
                '<button type="button" id="add-account-plan">Add Account Plan</button>'
            ),
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

    
    def save_model(self, request, obj, form, change):
        account_plans = []
        
        # Retrieve account plan data from POST
        plan_phases = request.POST.getlist('account_plans[]')
        plan_sizes = request.POST.getlist('account_size[]')
        plan_prices = request.POST.getlist('price[]')
        plan_daily_drawdowns = request.POST.getlist('daily_drawdown[]')
        plan_total_drawdowns = request.POST.getlist('total_drawdown[]')

        # Combine the retrieved data into account plans
        for i in range(len(plan_phases)):
            account_plan = {
                'phase': plan_phases[i],
                'account_size': plan_sizes[i],
                'price': plan_prices[i],
                'daily_drawdown': plan_daily_drawdowns[i],
                'total_drawdown': plan_total_drawdowns[i],
            }
            account_plans.append(account_plan)

        obj.account_plans = json.dumps(account_plans)
        super().save_model(request, obj, form, change)

    class Media:
        js = ('admin/js/propfirm_admin.js',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'approved')
    list_filter = ('approved',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
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
