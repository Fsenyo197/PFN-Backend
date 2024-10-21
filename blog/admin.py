# Core Django imports.
from django.contrib import admin

# Blog application imports.
from blog.models.article_model import Article
from blog.models.category_model import Category
from blog.models.discount_model import DiscountCode  # Import the DiscountCode model

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
    list_display = ('category', 'title', 'slug', 'status')
    list_filter = ('status', 'date_created', 'date_published',)
    search_fields = ('title', 'body',)
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date_published'
    ordering = ['status', '-date_created']
    readonly_fields = ('views', 'count_words', 'read_time')


@admin.register(DiscountCode)
class DiscountCodeAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for DiscountCode model.
    """
    list_display = ('firm_name', 'discount_code', 'discount_percentage', 'date', 'duration', 'is_active')
    list_filter = ('firm_name', 'discount_percentage', 'status', 'date')
    search_fields = ('firm_name', 'discount_code', 'title')
    ordering = ['status', '-date']
    readonly_fields = ('date_created', 'date_updated')
    
    def is_active(self, obj):
        return obj.is_active()
    is_active.boolean = True  # Display as a boolean checkmark
