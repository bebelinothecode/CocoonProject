from django.db import models


class Author(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    job_description = models.CharField(max_length=300)


class NewsArticle(models.Model):
    def __str__(self):
        return self.author_id

    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=400)
    content = models.CharField(max_length=800)
    published = models.BooleanField(default=False, blank=True)
    published_date = models.DateField()
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)


class NewsCategory(models.Model):
    def __str__(self):
        return self.newscategory
    newscategory = models.CharField(max_length=100)


class NewsArticleCategories(models.Model):
    def __str__(self):
        return "Article " + str(self.newsArticleID)
    newsArticleID = models.ForeignKey(NewsArticle, on_delete=models.CASCADE)
    newsCategoriesID = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
