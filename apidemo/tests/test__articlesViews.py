import json
from multiprocessing import AuthenticationError
from urllib import response
from django.test import TestCase,Client
from django.urls import reverse
from rest_framework.test import APITestCase,APIClient
class ArticlesViewTest(TestCase):
    fixtures = ['data_user.json','data_articles.json','data_category.json','data_group.json','data_groupUser.json']
    def setUp(self):
        loginApi_url= reverse('LoginApi')
        data={'UserName':'an','PassWord':'22122002'}
        responseLogin = Client().post(loginApi_url,data)
        self.articles_url = reverse('Articles')
        self.articlesById_url = reverse('ArticlesById',args=[1])
        self.articlesByCategory_url = reverse('ArticlesByCategory',args=['IT'])
        self.authorizationHeader = 'Bearer '+responseLogin.data['access']
        self.client= APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=self.authorizationHeader)
    def test_ArticlesApi_get(self):
        response = self.client.get(self.articles_url)
        self.assertEquals(response.status_code,200)
    def test_ArticlesApi_post(self):
        response = self.client.post(self.articles_url,{"User": 1,"Title": "Yêu cầu đối với nhân viên ngành IT","Content": "Làm mc hỏi và ghi nhớ nhanh hơn những trang giấy khô khan.","Category": 2},format='json')
        self.assertEquals(response.status_code,201)
    def test_ArticlesApiGetById_get(self):
        response= self.client.get(self.articlesById_url)
        self.assertEquals(response.status_code,200)
    def test_ArticlesApiGetById_patch(self):
        response= self.client.patch(self.articlesById_url,{"Title":"oke"},format='json')
        self.assertEquals(response.status_code,200)
    def test_ArticlesApiGetById_delete(self):
        response= self.client.delete(self.articlesById_url)
        self.assertEquals(response.status_code,204)
    def test_ArticlesByCategory_get(self):
        response= self.client.get(self.articlesByCategory_url)
        self.assertEquals(response.status_code,200)



