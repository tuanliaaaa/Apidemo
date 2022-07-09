import json
from urllib import response
from django.test import TestCase,Client
from django.urls import reverse
from rest_framework.test import APITestCase,APIClient
class GroupViewTest(TestCase):
    fixtures = ['data_user.json','data_articles.json','data_category.json','data_group.json','data_groupUser.json']
    def setUp(self):
        loginApi_url= reverse('LoginApi')
        data={'UserName':'an','PassWord':'22122002'}
        responseLogin = Client().post(loginApi_url,data)
        self.groups_url = reverse('GroupsApiAll')
        self.authorizationHeader = 'Bearer '+responseLogin.data['access']
        self.client= APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=self.authorizationHeader)
    def test_GroupsApiAll_get(self):
        response = self.client.get(self.groups_url)
        self.assertEquals(response.status_code,200)