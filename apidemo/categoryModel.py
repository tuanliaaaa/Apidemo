from django.db import models
class Category(models.Model):
    CategoryName = models.CharField(max_length=200)
    CategoryCodeParent = models.IntegerField()
    
    def __str__(self):
        return self.CategoryName +' '+ str(self.pk)