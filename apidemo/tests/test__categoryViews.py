import json
from multiprocessing import AuthenticationError
from urllib import response
from django.test import TestCase,Client
from django.urls import reverse
from rest_framework.test import APITestCase,APIClient
class CategoryViewTest(TestCase):
    fixtures = ['data_user.json','data_articles.json','data_category.json','data_group.json','data_groupUser.json']
    def setUp(self):
        loginApi_url= reverse('LoginApi')
        data={'UserName':'an','PassWord':'22122002'}
        responseLogin = Client().post(loginApi_url,data)
        self.authorizationHeader = 'Bearer '+responseLogin.data['access']
        self.categoriesApiAll_url = reverse('CategoriesApiAll')
        self.categoriesApiByid_url = reverse('CategoriesApiByid',args=[1])
        self.categoriesViewChilden_url = reverse('CategoriesViewChilden',args=[1])
        self.categoriesViewParent_url = reverse('CategoriesViewParent', args=[1])
        self.catrgoriesTreeView_url = reverse('CatrgoriesTreeView')
        self.client= APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=self.authorizationHeader)
    def test_CategoriesApiAll_get(self):
        response = self.client.get(self.categoriesApiAll_url)
        self.assertEquals(response.status_code,200)
    def test_CategoriesApiAll_post(self):
        response = self.client.post(self.categoriesApiAll_url,{"CategoryName":"EU","CategoryCodeParent":2},format='json')
        self.assertEquals(response.status_code,201)
    def test_CategoriesApiByid_get(self):
        response = self.client.get(self.categoriesApiByid_url)
        self.assertEquals(response.status_code,200)
    def test_test_CategoriesApiByid_patch(self):
        response = self.client.patch(self.categoriesApiByid_url,{"CategoryName":"EU"},format='json')
        self.assertEquals(response.status_code,200)
    def test_test_CategoriesApiByid_delete(self):
        response = self.client.delete(self.categoriesApiByid_url,{"CategoryName":"EU"},format='json')
        self.assertEquals(response.status_code,204)
    def test_CategoriesViewChilden_get(self):
        response = self.client.get(self.categoriesViewChilden_url)
        self.assertEquals(response.status_code,200)
    def test_CategoriesViewParent_get(self):
        response = self.client.get(self.categoriesViewParent_url)
        self.assertEquals(response.status_code,200)
    def test_CatrgoriesTreeView_get(self):
        response = self.client.get(self.catrgoriesTreeView_url)
        self.assertEquals(response.status_code,200)