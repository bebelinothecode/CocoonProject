from rest_framework import serializers
from .models import Author, NewsArticle, NewsCategory, NewsArticleCategories
from rest_framework.fields import CharField, EmailField


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'


class ArticlesSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsArticle
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsCategory
        fields = '__all__'
