from django.test import TestCase
from ..userModel import User
class UserTest(TestCase):
    def create_user(self,UserName="tuan",Age="20",Email="nhattuan44t@gmail.com",Password="22122002"):
        return  User.objects.create(UserName=UserName,Age=Age,Email=Email,Password=Password)
    def test_user_creation(self):
        user = self.create_user()
        self.assertTrue(isinstance(user,User))
        self.assertEqual(user.__str__(),str(user.pk))