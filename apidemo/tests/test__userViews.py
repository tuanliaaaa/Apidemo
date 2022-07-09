import json
from multiprocessing import AuthenticationError
from urllib import response
from django.test import TestCase,Client
from django.urls import reverse
from rest_framework.test import APITestCase,APIClient
class UserViewTest(TestCase):
    fixtures = ['data_user.json','data_articles.json','data_category.json','data_group.json','data_groupUser.json']
    def setUp(self):
        loginApi_url= reverse('LoginApi')
        data={'UserName':'an','PassWord':'22122002'}
        responseLogin = Client().post(loginApi_url,data)
        self.userInformationByToken_url = reverse('UserInformationByToken')
        self.userApiGetAll_url = reverse('UserApiGetAll')
        self.userApiGetById_url = reverse('UserApiGetById',args=[1])
        self.authorizationHeader = 'Bearer '+responseLogin.data['access']
        self.client= APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=self.authorizationHeader)
    def test_ArticlesApi_get(self):
        response = self.client.get(self.userInformationByToken_url)
        self.assertEquals(response.status_code,200)
    def test_UserApiGetAll_get(self):
        response = self.client.get(self.userApiGetAll_url)
        self.assertEquals(response.status_code,200)
    def test_UserApiGetAll_get(self):
        response = self.client.post(self.userApiGetAll_url,{"UserName":"tuan","Age":12,"Email":"nhat@gmail.com","Password":"22122002"},format='json')
        self.assertEquals(response.status_code,201)
    def test_UserApiGetById_get(self):
        response = self.client.get(self.userApiGetById_url)
        self.assertEquals(response.status_code,200)
    def test_UserApiGetById_patch(self):
        response = self.client.patch(self.userApiGetById_url,{"UserName":"thanh"},format='json')
        self.assertEquals(response.status_code,200)
    def test_UserApiGetById_delete(self):
        response = self.client.delete(self.userApiGetById_url)
        self.assertEquals(response.status_code,204)