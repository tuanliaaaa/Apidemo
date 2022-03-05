from django.contrib import admin
from .articlesModel import Articles
from .userModel import User
from .categoryModel import Category
# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Articles)
