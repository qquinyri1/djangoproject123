from django.db import models

# Create your models here.
from django.db import models


class Author(models.Model):
    fullname = models.CharField(max_length=100, unique=True)
    born_date = models.DateField(default=None, null=True)  # %B %d, %Y - March 14, 1879
    born_location = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)


class Quote(models.Model):
    quote = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)