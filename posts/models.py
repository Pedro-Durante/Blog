from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=75)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    slug = models.SlugField()
    banner = models.ImageField(default='logo-poli.png', blank = True)
    def __str__(self):
        return self.title