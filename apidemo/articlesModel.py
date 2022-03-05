from django.db import models
from .userModel import User
from .categoryModel import Category
class Articles(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    Title = models.CharField(max_length=200)
    Content = models.TextField()
    Category=models.ForeignKey(Category,related_name='tasks',on_delete=models.CASCADE)