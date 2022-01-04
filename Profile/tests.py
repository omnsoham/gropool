from django.test import TestCase
# Create your tests here.
from django.contrib import auth
from .models import *

class AuthTestCase(TestCase):
    def setUp(self):
        self.u = UserInfo.objects.create_user('usernamei', 'passwordi', 'testcase@test.org', 99999)
        self.u.is_staff = True
        self.u.is_superuser = True
        self.u.is_active = True
        self.u.save()

    def testLogin(self):
        self.client.login(username='usernamei', password='passwordi')