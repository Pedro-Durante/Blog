from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Category(models.Model):
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'
    
class Post(models.Model):
    title = models.CharField(max_length=75)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    slug = models.SlugField()
    banner = models.ImageField(default='logo-poli.png', blank = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    categories = models.ManyToManyField(Category, related_name='posts')
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.body}" - {self.author.username}'
    