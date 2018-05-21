#tests.py
from django.contrib.auth.models import User
from lop.forms import SignUpForm
from lop.models import Profile
from django.urls import reverse
from django.test.client import Client
from django.contrib import auth
import unittest


class ProfileTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()
    def testProfilePage(self):
        username = 'testuser'
        self.client.login(username= username, password='loptestuserpassword')
        response = self.client.get('/viewprofile/' + username)
        self.assertEqual(response.status_code, 200)

class SignupFormTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def testSignupForm(self):
        form_data = {"username": "mytestuser1", "first_name": "Test", "last_name": "User",
                     "email": "mytestuser1@localhost.com", "password1":"12345", "password2": "12345"
                    }
        response = self.client.post("/signup/", form_data)
        print(response.status_code)
        self.assertEqual(response.status_code, 200)

class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'testuser@testlop.com', 'loptestuserpassword')


    def testLogin(self):
        user = self.client.login(username='testuser', password='loptestuserpassword')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class SignupPageTestCaseResponse(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def testSignupResponse(self):
        response = self.client.get('/signup/')
        self.assertEqual(response.status_code, 200)


class ChangePasswordFormTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def testChangePasswordForm(self):
        form_data = {"old_password": "12345", "new_password1": "123456",
                     "new_password2": "123456"
                    }
        response = self.client.post("/password", form_data, follow=True)
        self.assertEqual(response.status_code, 200)

class LogoutTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def testLogout(self):
        self.client.login(username='testuser', password='loptestuserpassword')
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 200)
