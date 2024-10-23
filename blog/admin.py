from django.contrib import admin
from blog.models.article_model import Article
from blog.models.category_model import Category

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
    list_display = ('category', 'title', 'slug', 'status', 'discount_code', 'firm_name', 'discount_percentage', 'duration')
    list_filter = ('status', 'date_created', 'date_published',)
    search_fields = ('title', 'body',)
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date_published'
    ordering = ['status', '-date_created']
    
    # Add date_created and date_updated to readonly fields
    readonly_fields = ('views', 'count_words', 'read_time', 'date_created', 'date_updated')

    # Adding the discount-specific fields to the form
    fieldsets = (
        (None, {
            'fields': ('category', 'title', 'slug', 'body', 'status', 'image', 'image_credit', 'meta_description', 'meta_keywords', 'date_published', 'views', 'count_words', 'read_time')
        }),
        ('Discount Information', {
            'fields': ('firm_name', 'discount_code', 'discount_percentage', 'duration', 'website_domain'),
            'classes': ('collapse',),  # Make this section collapsible
        }),
    )

    # Optionally, you can define which fields are editable
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('slug',)  # Prevent slug editing for existing objects
        return self.readonly_fields
