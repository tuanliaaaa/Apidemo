from telnetlib import STATUS
from django.test import TestCase,Client
from django.urls import reverse
class LoginViewTest(TestCase):
    def setUp(self):
        self.client= Client()
        self.login_url = reverse('Login')
    def test_login_get(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'login.html')