import json
from urllib import response
from django.test import TestCase,Client
from django.urls import reverse
from rest_framework.test import APITestCase,APIClient
class GroupUserViewTest(TestCase):
    fixtures = ['data_user.json','data_articles.json','data_category.json','data_group.json','data_groupUser.json']
    def setUp(self):
        self.groupUser_url = reverse('GetUserAndGroupOfUser')
        self.client= APIClient()
    def test_GetUserAndGroupOfUser_get(self):
        response = self.client.get(self.groupUser_url)
        self.assertEquals(response.status_code,200)
    def test_GetUserAndGroupOfUser_post(self):
        response = self.client.post(self.groupUser_url,{"UserName":"an","ListGroup":["Admin"]},format='json')
        self.assertEquals(response.status_code,200)
