from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'faculty']
    search_fields = ['title', 'summary', 'news_reference', 'faculty__name']
    list_filter = ['date', 'faculty']

admin.site.register(News, NewsAdmin)