from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
#Импорт моделей
from .models import Post
from django.core.paginator import Paginator

#Импорт настроек

from django.conf import settings


# Create your views here.

def ListOfPosts(request):
    posts_per_page = getattr(settings,'BLOG_POSTS_PER_PAGE',3)
    """Выбираем все посты со статусом Опубликовано"""
    posts = Post.objects.filter(status='published')
    # Инициализируем объект пагинатор
    paginator = Paginator(posts,posts_per_page)
    # Обращаемся к словарю GET с целью получения номера текущей страницы
    current_page = request.GET.get('page')
    page_obj = paginator.get_page(current_page)
    # Возвращаем страницу блога с параметрами
    return render(request, 'blog/blog.html',
                   {'page_obj': page_obj,
                   'title':'Блог сайта о книгах',
                   "paginator": paginator,})
