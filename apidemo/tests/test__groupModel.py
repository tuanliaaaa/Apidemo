
from django.test import TestCase
from ..groupModel import Group
class GroupTest(TestCase):
    def create_group(self,GroupName="TestAdmin"):
        return Group.objects.create(GroupName=GroupName)
    def test_group_creation(self):
        group = self.create_group()
        self.assertTrue(isinstance(group, Group))
        self.assertEqual(group.__str__(), group.GroupName)