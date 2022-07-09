from telnetlib import STATUS
from django.test import TestCase,Client
from django.urls import reverse
class SignupViewTest(TestCase):
    def setUp(self):
        self.client= Client()
        self.signup_url = reverse('Signup')
    def test_login_get(self):
        response = self.client.get(self.signup_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'signup.html')