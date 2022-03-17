from ast import Pass
from django.db import models
from .groupUserModel import GroupUser
class User(models.Model):
    UserName = models.CharField(max_length=200)
    Age = models.IntegerField()
    Email = models.EmailField()
    PassWord = models.CharField(max_length=100)
    GroupUser =models.ForeignKey(GroupUser,on_delete=models.CASCADE)
