from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
#Импорт моделей
from .models import Post



# Create your views here.

def ListOfPosts(request):
    """Выбираем все посты со статусом Опубликовано"""
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})