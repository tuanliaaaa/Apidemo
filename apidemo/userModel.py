from ast import Pass
from django.db import models
class User(models.Model):
    UserName = models.CharField(max_length=200)
    Age = models.IntegerField()
    Email = models.EmailField()
    PassWord = models.CharField(max_length=100)
    
