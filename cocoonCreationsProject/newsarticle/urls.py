from django.urls import path

from . import views
from .views import AuthorList, NewsCategoryList, ArticlesList

urlpatterns = [
    path('authors/', AuthorList.as_view()),
    path('newscategory/', NewsCategoryList.as_view()),
    path('articles/', ArticlesList.as_view()),
    path('', views.index, name="index"),
]
