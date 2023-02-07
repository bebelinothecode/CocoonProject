from .models import Author, NewsCategory, NewsArticle
from .serializers import AuthorSerializer, ArticlesSerializer, CategoriesSerializer
from django.http import HttpResponse
from rest_framework import generics


def index(request):
    return HttpResponse("Hello, world. This is Cocoon Creations Test.")


class NewsCategoryList(generics.ListAPIView):
    serializer_class = CategoriesSerializer

    def get_queryset(self):
        queryset = NewsCategory.objects.all()
        location = self.request.query_params.get('newscategory')
        #
        if location is not None:
            queryset = queryset.filter(newscategory=location)
        return queryset


class ArticlesList(generics.ListAPIView):
    serializer_class = ArticlesSerializer

    def get_queryset(self):
        queryset = NewsArticle.objects.all()
        location = self.request.query_params.get('id')

        if location is not None:
            queryset = queryset.filter(id=id)
        return queryset


class AuthorList(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer

    def get_queryset(self):
        queryset = Author.objects.all()
        location = self.request.query_params.get('id')

        if location is not None:
            queryset = queryset.filter(id=id)
        return queryset


