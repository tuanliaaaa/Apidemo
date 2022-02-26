from django.db import models

# Create your models here.
class User(models.Model):
    UserName = models.CharField(max_length=200)
    Age = models.IntegerField()
    email = models.EmailField()
class Category(models.Model):
    CategoryName = models.CharField(max_length=200)
    CategoryCodeParent = models.IntegerField()
class Post(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    Category=models.ForeignKey(Category,related_name='tasks',on_delete=models.CASCADE)