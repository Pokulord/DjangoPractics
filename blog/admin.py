from django.contrib import admin
from .models import Post
# Register your models here.

"""Настройка отображения"""
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','body','date_of_publish','created','updated','status')
    #Автозаполнение поля slug (передаём словарь)
    prepopulated_fields = {
        'slug': ('title',)
    }
    # Добавляем фильтры
    list_filter = ('author','created','status')
    # Поиск по записям 
    search_fields = ('title','body')
    raw_id_fields = ('author',)
    

admin.site.register(Post,PostAdmin)