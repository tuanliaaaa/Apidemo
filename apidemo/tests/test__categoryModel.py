
from django.test import TestCase
from ..categoryModel import Category
class CategoryTest(TestCase):
    def create_category(self,CategoryName="IT",CategoryCodeParent=0):
        return Category.objects.create(CategoryName=CategoryName,CategoryCodeParent=CategoryCodeParent)
    def test_category_creation(self):
        category = self.create_category()
        self.assertTrue(isinstance(category, Category))
        self.assertEqual(category.__str__(), category.CategoryName +' '+ str(category.pk))