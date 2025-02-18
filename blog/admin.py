from django.contrib import admin
from blog.models.propfirm_model import PropFirm, AccountPlan
from blog.models.article_model import Article
from blog.models.category_model import Category
from blog.forms.dashboard.propfirm_form import PropFirmForm
from blog.models.apikeys_model import APIKey
from django_summernote.admin import SummernoteModelAdmin


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
        'account_type',
        'account_size',
        'price',
        'leverage',
        'profit_split_ratio',
        'profit_target',
        'daily_drawdown',
        'total_drawdown',
        'minimum_trading_days',
        'phase_time_limit',
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
        'slug',
        'year_established',
        'firm_type',
        'location',
        'status',
        'is_active',
    )
    search_fields = ('name', 'location', 'firm_type')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('firm_type', 'drawdown_type', 'payout_frequency', 'status', 'date_created', 'date_published', 'is_active')
    readonly_fields = ( 'date_created', 'date_updated')
    date_hierarchy = 'date_published'
    ordering = ['status', '-date_created']

    fieldsets = (
        (None, {
            'fields': (
                'name', 'slug', 'about', 'website', 'year_established', 'firm_type', 'location',
                'drawdown_type', 'payout_frequency', 'is_active', 'status',
            ),
        }),
        ('Features', {
            'fields': ('weekend_holding_rule', 'copy_trading_rule', 'two_percent_rule', 'stop_loss_rule', 'vpn_and_vps_rule', 'consistency_rule'),
        }),
        ('Options', {
            'fields': ('payout_options', 'payment_options'),
        }),
        ('Platforms', {
            'fields': ('trading_platforms',),
        }),
        ('Restrictions', {
            'fields': ('countries_prohibited',),
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
class ArticleAdmin(SummernoteModelAdmin):
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

    summernote_fields = ('body',)  # Apply Summernote to the 'body' field

    fieldsets = (
        (None, {
            'fields': (
                'category', 'title', 'slug',
                ('image', 'image_url'),
                'image_credit', 'body', 'status',
                'meta_description', 'meta_keywords',
                'date_published', 'views', 'count_words', 'read_time',
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

    def save_model(self, request, obj, form, change):
        """
        Ensure validation for either `image` or `image_url` when saving via admin.
        """
        if obj.image and obj.image_url:
            raise ValueError("Provide either an uploaded image or a Cloudinary image link, not both.")
        if not obj.image and not obj.image_url:
            raise ValueError("You must provide either an uploaded image or a Cloudinary image link.")
        super().save_model(request, obj, form, change)
