from django.shortcuts import render, redirect, get_object_or_404
from blog.models.article_model import Article
from blog.services.article_service import ArticleService
from blog.repositories.article_repository import ArticleRepository

# Initialize the service with the repository
article_service = ArticleService(repository=ArticleRepository())

def article_list(request):
    articles = article_service.get_all_articles()
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, article_id):
    article = article_service.get_article_by_id(article_id)
    if article is None:
        return redirect('article_list')  # Handle not found
    return render(request, 'articles/article_detail.html', {'article': article})

def article_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author_id = request.POST['author_id']
        category_id = request.POST['category_id']
        article_service.create_article(title, content, author_id, category_id)
        return redirect('article_list')
    return render(request, 'articles/article_form.html')

def article_update(request, article_id):
    article = article_service.get_article_by_id(article_id)
    if article is None:
        return redirect('article_list')  # Handle not found
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        article_service.update_article(article_id, title, content)
        return redirect('article_detail', article_id=article.id)
    return render(request, 'articles/article_form.html', {'article': article})

def article_delete(request, article_id):
    article_service.delete_article(article_id)
    return redirect('article_list')
