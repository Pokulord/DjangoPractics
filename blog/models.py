from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

"""Класс, который отвечает за модель постов в блоге"""

class Post(models.Model):
    """Константа, содержащая статусы публикации поста"""
    STATUSES = (
        ('draft','Draft'),
        ('published', 'Published')
    )
    """Поля модели"""
    #Заголовок поста
    title = models.CharField(max_length = 250)
    #Адрес статьи, который подставляется в глобальный адрес
    #Он уникален для каждой статьи
    slug = models.SlugField(max_length=250, unique_for_date= 'publish_date')
    #Автор статьи
    author = models.ForeignKey(User, related_name= 'blog_posts',default='Svyatoslav', on_delete=models.CASCADE)
    # "Тело" статьи. Непосредственно её содержание
    body = models.TextField(default='empty')
    #Дата публикации
    date_of_publish = models.DateTimeField(default=timezone.now)
    # Когда был создан пост
    #auto_now_add отвечает за автоматическое добавление даты в строку БД
    created = models.DateTimeField(auto_now_add=True)
    #Когда запись была обновлена
    updated = models.DateTimeField(auto_now=True)
    #Статус поста
    status = models.CharField(max_length=20, choices=STATUSES, default='draft')


class Meta:
    #Сортировка по убыванию
    ordering = ('-publish_date')



def __str__(self):
    return self.title


