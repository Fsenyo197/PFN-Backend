from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View
from blog.forms.dashboard.category_forms import CategoryCreateForm, CategoryUpdateForm
from blog.models.category_model import Category


class CategoryListView(View):
    template_name = 'dashboard/category/category_list.html'

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, self.template_name, context)


class CategoryCreateView(View):
    template_name = 'dashboard/category/category_create_form.html'

    def get(self, request, *args, **kwargs):
        category_create_form = CategoryCreateForm()
        context = {"category_create_form": category_create_form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        category_create_form = CategoryCreateForm(request.POST)

        if category_create_form.is_valid():
            category_create_form.save()
            messages.success(request, "Category created successfully.")
            return redirect("blog:category_list")
        
        context = {"category_create_form": category_create_form}
        messages.error(request, "Please fill required fields")
        return render(request, self.template_name, context)


class CategoryUpdateView(View):
    template_name = 'dashboard/category/category_update_form.html'

    def get(self, request, *args, **kwargs):
        category = get_object_or_404(Category, id=self.kwargs.get("id"))
        category_update_form = CategoryUpdateForm(instance=category)
        context = {"category_update_form": category_update_form, "category": category}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        category = get_object_or_404(Category, id=self.kwargs.get("id"))
        category_update_form = CategoryUpdateForm(request.POST, instance=category)

        if category_update_form.is_valid():
            category_update_form.save()
            messages.success(request, "Category updated successfully.")
            return redirect("blog:category_list")

        context = {"category_update_form": category_update_form, "category": category}
        messages.error(request, "Please fill required fields")
        return render(request, self.template_name, context)


class CategoryDeleteView(View):
    def get(self, *args, **kwargs):
        category = get_object_or_404(Category, id=self.kwargs.get("id"))
        category.delete()
        messages.success(self.request, "Category deleted successfully.")
        return redirect('blog:category_list')


class CategoryDetailView(View):
    template_name = 'dashboard/category/category_detail.html'

    def get(self, request, *args, **kwargs):
        category = get_object_or_404(Category, id=self.kwargs.get("id"))
        context = {'category': category}
        return render(request, self.template_name, context)
