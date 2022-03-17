
from django.db import models
class GroupUser(models.Model):
    GroupName = models.CharField(max_length=225)
    GroupCode = models.IntegerField()