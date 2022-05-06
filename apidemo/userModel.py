from ast import Pass
from django.db import models
class User(models.Model):
    UserName = models.CharField(max_length=200)
    Age = models.IntegerField(null=True)
    Email = models.EmailField()
    Password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.UserName