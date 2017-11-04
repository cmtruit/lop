#tests.py
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test.client import Client
import unittest

class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'testuser@testlop.com', 'loptestuserpassword')

    def testLogin(self):
        self.client.login(username='testuser', password='loptestuserpassword')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class LogoutTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def testLogout(self):
        self.client.login(username='testuser', password='loptestuserpassword')
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 200)
