from django.test import TestCase
from omniventure_app.forms import *

class MemberFormTest(TestCase):
    def test_member_form_valid(self):
        form_data = {
            'name': 'Test Member',
            'pronouns': 'He/Him',
            'active_times': 'Evenings',
            'about': 'Lorem ipsum dolor sit amet',
            'discord': 'test_user#1234',
            'discord_message_check': False,
            'image': None  # Set to None or provide a mock file
        }
        form = member_form(data=form_data)
        self.assertTrue(form.is_valid())

    def test_member_form_invalid(self):
        # Test invalid form data
        invalid_form_data = {
            # Missing required fields
        }
        form = member_form(data=invalid_form_data)
        self.assertFalse(form.is_valid())

class CharacterFormTest(TestCase):
    def test_character_form_valid(self):
        form_data = {
            'character_id': '123456',
            'background': 'Lorem ipsum dolor sit amet',
            'personality': 'Friendly and outgoing',
            'pronouns': 'He/Him'
        }
        form = CharacterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_character_form_invalid(self):
        # Test invalid form data
        invalid_form_data = {
            # Missing required fields
        }
        form = CharacterForm(data=invalid_form_data)
        self.assertFalse(form.is_valid())

class LoginFormTest(TestCase):
    def test_login_form_valid(self):
        form_data = {
            'username': 'test_user',
            'password': 'test_password'
        }
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_login_form_invalid(self):
        # Test invalid form data
        invalid_form_data = {
            # Missing required fields
        }
        form = LoginForm(data=invalid_form_data)
        self.assertFalse(form.is_valid())
