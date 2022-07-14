from django.db import models
from .userModel import User
from .categoryModel import Category
class Articles(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    Title = models.CharField(max_length=200)
    Content = models.CharField(max_length=200000)
    Category=models.ForeignKey(Category,related_name='tasks',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Title