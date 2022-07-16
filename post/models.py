from django.db import models


class Author(models.Model):
    pass


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=50)
    content = models.TextField(max_length=500)
    image = models.ImageField()
    time_read = models.IntegerField()
    status = models.BooleanField(default=False)
