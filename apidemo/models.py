from django.db import models

# Create your models here.
class User(models.Model):
    UserName = models.CharField(max_length=200)
    Age = models.IntegerField()
    Email = models.EmailField()
class Category(models.Model):
    CategoryName = models.CharField(max_length=200)
    CategoryCodeParent = models.IntegerField()
class Articles(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    Title = models.CharField(max_length=200)
    Content = models.TextField()
    Category=models.ForeignKey(Category,related_name='tasks',on_delete=models.CASCADE)