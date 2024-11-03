from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=75)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    slug = models.SlugField()
    banner = models.ImageField(default='logo-poli.png', blank = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.title