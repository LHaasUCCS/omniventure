from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from omniventure_app.models import *
from unittest.mock import patch
from omniventure_app.forms import CharacterForm

class MemberViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test user
        cls.user = User.objects.create_user(username='test_user', password='test_password')

    def test_index_view(self):
        # Test the index view
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'omniventure_app/index.html')

    def test_member_list_view(self):
        # Test the member list view
        response = self.client.get(reverse('member_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'omniventure_app/member_list.html')

class RegisterViewTest(TestCase):
    def test_register_view_get(self):
        # Test GET request to register view
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'omniventure_app/register.html')




