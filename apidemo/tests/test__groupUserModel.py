
import re
from django.test import TestCase
from ..groupModel import Group
from ..groupUserModel import GroupUser
from ..userModel import User
class GroupUserTest(TestCase):
    def create_group(self,GroupName="TestAdmin"):
        return Group.objects.create(GroupName=GroupName)
    def create_user(self,UserName="tuan",Age="20",Email="nhattuan44t@gmail.com",Password="22122002"):
        return  User.objects.create(UserName=UserName,Age=Age,Email=Email,Password=Password)
    def create_groupUser(self,Group,User):
        return GroupUser.objects.create(Group=Group,User=User)
    def test_groupUser_creation(self):
        group = self.create_group()
        user = self.create_user()
        groupUser= self.create_groupUser(group,user)
        self.assertTrue(isinstance(groupUser,GroupUser))
        self.assertEqual(groupUser.__str__(), 'Group: '+groupUser.Group.GroupName +' User: '+groupUser.User.UserName)