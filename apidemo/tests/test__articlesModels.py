from unicodedata import category
from django.test import TestCase
from ..articlesModel import Articles
from ..userModel import User
from ..categoryModel import Category
class ArticlesTest(TestCase):
    def create_category(self,CategoryName="IT",CategoryCodeParent=0):
        return Category.objects.create(CategoryName=CategoryName,CategoryCodeParent=CategoryCodeParent)
    def create_user(self,UserName="tuan",Age="20",Email="nhattuan44t@gmail.com",Password="22122002"):
        return  User.objects.create(UserName=UserName,Age=Age,Email=Email,Password=Password)

    def create_articles(self,User,Category,Title="ArticlesTest",Content="ContentArticlesTest"):
        return Articles.objects.create(User=User,Title = Title,Content = Content , Category = Category)

    def test_articles_creation(self):

        user = self.create_user()
        category = self.create_category()
        article = self.create_articles(user,category)
        self.assertTrue(isinstance(article, Articles))
        self.assertEqual(article.__str__(), article.Title)