from .groupModel import Group
from .userModel import User
from django.db import models
class GroupUser(models.Model):
    Group=models.ForeignKey(Group,on_delete=models.CASCADE,null=True)
    User=models.ForeignKey(User,on_delete=models.CASCADE,null=True)