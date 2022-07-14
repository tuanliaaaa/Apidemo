from urllib import response
import django
from django.test import TestCase, Client
from rest_framework.test import APITestCase
import json
from ..userModel import User
from django.urls import reverse
class TokenTestViews(APITestCase):
    fixtures = ['data_user.json']
    def setUp(self):
        self.client= Client()
        self.loginApi_url= reverse('LoginApi')
        self.user={'UserName':'ok','PassWord':'nhattuan'}
    def test_token_create(self):
        data={'UserName':'an','PassWord':'22122002'}
        response = self.client.post(self.loginApi_url,data)
        self.assertEquals(response.status_code,200)