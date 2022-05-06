from django.db import models
class Group(models.Model):
    GroupName = models.CharField(max_length=225)
    
    def __str__(self) :
        return self.GroupName
    