from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

#def index(request):
#    return HttpResponse('Hello Django!')

def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})

