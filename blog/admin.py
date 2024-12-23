from django.contrib import admin
from blog.models.propfirm_model import PropFirm, AccountPlan
from blog.models.article_model import Article
from blog.models.category_model import Category
from blog.forms.dashboard.propfirm_form import PropFirmForm
from blog.models.apikeys_model import APIKey


@admin.register(APIKey)
class APIKeyAdmin(admin.ModelAdmin):
    list_display = ('user', 'key', 'is_active', 'created_at', 'last_used')
    list_filter = ('is_active', 'created_at', 'last_used')
    search_fields = ('user__username', 'key')
    readonly_fields = ('key', 'secret', 'created_at', 'last_used')

    def revoke_keys(self, request, queryset):
        queryset.update(is_active=False)
        self.message_user(request, "Selected keys have been revoked.")

    actions = ['revoke_keys']

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


class AccountPlanInline(admin.TabularInline):
    model = AccountPlan
    extra = 1
    fields = (
        'phase',
        'account_size',
        'price',
        'profit_split_ratio',
        'minimum_trading_days',
        'leverage',
        'daily_drawdown',
        'total_drawdown',
        'currency',
        'is_available',
        'status',
    )


@admin.register(PropFirm)
class PropFirmAdmin(admin.ModelAdmin):
    form = PropFirmForm
    inlines = [AccountPlanInline]

    list_display = (
        'name',
        'website',
        'year_established',
        'firm_type',
        'location',
        'status',
        'is_active',
    )
    search_fields = ('name', 'location', 'firm_type')
    list_filter = ('firm_type', 'drawdown_type', 'payout_frequency', 'status', 'date_created', 'date_published', 'is_active')
    readonly_fields = ( 'date_created', 'date_updated')
    date_hierarchy = 'date_published'
    ordering = ['status', '-date_created']

    fieldsets = (
        (None, {
            'fields': (
                'name', 'website', 'year_established', 'firm_type', 'location',
                'drawdown_type', 'payout_frequency', 'is_active', 'status',
            ),
        }),
        ('Features', {
            'fields': ('expert_advisors', 'copy_trading', 'two_percent_rule', 'stop_loss_rule', 'consistency_rule'),
        }),
        ('Options', {
            'fields': ('payout_options', 'payment_options'),
        }),
        ('Restrictions', {
            'fields': ('countries_prohibited',),
        }),
        ('Platforms', {
            'fields': ('trading_platforms',),
        }),
    )


@admin.register(AccountPlan)
class AccountPlanAdmin(admin.ModelAdmin):
    list_display = (
        'prop_firm',
        'phase',
        'account_size',
        'price',
        'currency',
        'is_available',
        'status',
    )
    list_filter = ('phase', 'currency', 'is_available', 'status')
    search_fields = ('prop_firm__name', 'phase', 'account_size')
    ordering = ['prop_firm', 'phase', 'account_size']


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
        'duration',
    )
    list_filter = ('status', 'date_created', 'date_published')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date_published'
    ordering = ['status', '-date_created']

    readonly_fields = ('views', 'count_words', 'read_time', 'date_created', 'date_updated')

    fieldsets = (
        (None, {
            'fields': (
                'category', 'title', 'slug', 'image', 'image_credit', 'body',
                'status', 'meta_description', 'meta_keywords', 'date_published',
                'views', 'count_words', 'read_time',
            ),
        }),
        ('Discount Information', {
            'fields': (
                'firm_name', 'discount_code', 'discount_percentage',
                'duration', 'website_domain',
            ),
            'classes': ('collapse',),
        }),
    )
