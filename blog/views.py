from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

#def index(request):
#    return HttpResponse('Hello Django!')

def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})

def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})

def edit_page(request, article_id):
    id = str(article_id)
    if id == '0':
        return render(request, 'blog/edit_page.html')
    else:
        article = models.Article.objects.get(pk=article_id)
        return render(request, 'blog/edit_page.html', {'article': article})

def edit_action(request):
    id = request.POST.get('id', '0')
    print('id:' + id)
    title = request.POST.get('title', 'Title')
    content = request.POST.get('content', 'CONTENT')
    if id == '0':
        print('create')
        models.Article.objects.create(title=title, content=content)
    else:
        print('update')
        article = models.Article.objects.get(pk=id)
        article.title = title
        article.content = content
        article.save()

    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})

