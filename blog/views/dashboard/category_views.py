from django.shortcuts import render, redirect, get_object_or_404
from blog.models.category_model import Category
from blog.services.category_service import CategoryService
from blog.repositories.category_repository import CategoryRepository

# Initialize the service with the repository
category_service = CategoryService(repository=CategoryRepository())

def category_list(request):
    categories = category_service.get_all_categories()
    return render(request, 'categories/category_list.html', {'categories': categories})

def category_detail(request, category_id):
    category = category_service.get_category_by_id(category_id)
    if category is None:
        return redirect('category_list')  # Handle not found
    return render(request, 'categories/category_detail.html', {'category': category})

def category_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        category_service.create_category(name)
        return redirect('category_list')
    return render(request, 'categories/category_form.html')

def category_update(request, category_id):
    category = category_service.get_category_by_id(category_id)
    if category is None:
        return redirect('category_list')  # Handle not found
    if request.method == 'POST':
        name = request.POST['name']
        category_service.update_category(category_id, name)
        return redirect('category_detail', category_id=category.id)
    return render(request, 'categories/category_form.html', {'category': category})

def category_delete(request, category_id):
    category_service.delete_category(category_id)
    return redirect('category_list')
