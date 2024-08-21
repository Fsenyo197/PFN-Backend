# Core Django imports.
from django.contrib import admin

# Blog application imports.
from blog.models.article_model import Article
from blog.models.category_model import Category


class ProfileAdmin(admin.ModelAdmin):
    list_filter = ('user',)
    search_fields = ('user',)
    ordering = ['user', ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'approved')
    list_filter = ('name', 'approved',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name', ]


# Registers the category model at the admin backend.
admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'slug', 'status')
    list_filter = ('status', 'date_created', 'date_published',)
    search_fields = ('title', 'body',)
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date_published'
    ordering = ['status', '-date_created', ]
    readonly_fields = ('views', 'count_words', 'read_time')


# Registers the article model at the admin backend.
admin.site.register(Article, ArticleAdmin)
