from django.db import models

# Create your models here.
"""Модель списка книг"""
class ListOfBooks(models.Model):
    """Наименование книги"""
    name = models.CharField(max_length=250)
    """Цена книги"""
    price = models.DecimalField(max_digits=20,decimal_places=2)
    """Автор книги"""
    author = models.CharField(max_length=250)
    """Есть ли скидка"""
    discount = models.IntegerField(default=0)
    """Ссылка на товар"""
    slug = models.SlugField(max_length=250,unique=True,default="empty")
