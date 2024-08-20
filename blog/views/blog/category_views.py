# Core Django imports.
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView
)

# Blog application imports.
from blog.models.article_model import Article
from blog.models.category_model import Category


class CategoryArticlesListView(ListView):
    model = Article
    paginate_by = 12
    context_object_name = 'articles'
    template_name = 'blog/category/category_articles.html'

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        return Article.objects.filter(category=category, status=Article.PUBLISHED, deleted=False)

    def get_context_data(self, **kwargs):
        context = super(CategoryArticlesListView, self).get_context_data(**kwargs)
        category = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        context['category'] = category
        return context


class CategoriesListView(ListView):
    model = Category
    paginate_by = 12
    context_object_name = 'categories'
    template_name = 'blog/category/categories_list.html'

    def get_queryset(self):
        return Category.objects.order_by('-date_created')


class CategoryCreateView(SuccessMessageMixin, CreateView):
    model = Category
    fields = ["name", "image"]
    template_name = 'blog/category/category_form.html'

    def form_valid(self, form):
        form.instance.save()
        messages.success(self.request, f"'{form.instance.name}' submitted successfully.")
        return redirect('/')


class CategoryUpdateCreateView(SuccessMessageMixin, UpdateView):
    model = Category
    fields = ["name", "image"]
    template_name = 'blog/category/category_form.html'
    success_url = reverse_lazy("blog:categories_list")
    success_message = "Category Updated Successfully"
