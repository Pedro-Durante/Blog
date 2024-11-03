from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=16)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=75)
    
    def __str__(self):
        return self.name