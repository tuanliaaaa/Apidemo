from django.contrib import admin
from .articlesModel import Articles
from .userModel import User
from .groupModel import Group
from .categoryModel import Category
from .groupUserModel import GroupUser
# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Articles)
admin.site.register(GroupUser)
admin.site.register(Group)
