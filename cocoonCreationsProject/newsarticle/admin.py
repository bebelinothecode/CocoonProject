from django.contrib import admin

from .models import Author, NewsArticle, NewsCategory, NewsArticleCategories

admin.site.register(Author)
admin.site.register(NewsArticle)
admin.site.register(NewsCategory)
admin.site.register(NewsArticleCategories)

# Register your models here.
