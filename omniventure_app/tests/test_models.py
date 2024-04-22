from django.test import TestCase
from omniventure_app.models import *
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from PIL import Image


class member_test(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test user
        cls.user = User.objects.create_user(username='test_user', password='test_password')
        

    def test_can_edit_method(self):
        # Create a member
        member = Member.objects.create(name='Test Member', user=self.user)
        # Create another user
        another_user = User.objects.create_user(username='another_user', password='another_password')
        # Test if the first user can edit the member
        self.assertTrue(member.can_edit(self.user))
        # Test if the second user cannot edit the member
        self.assertFalse(member.can_edit(another_user))


class CharacterModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("performing character model test setup")
        cls.member = Member.objects.create(name='Test Member', user=User.objects.create_user(username='test_user', password='test_password'))

    def test_character_creation(self):
        print("Test character creation")
        character = Character.objects.create(
            character_id=1,
            name='Test Character',
            server='Test Server',
            data_center='Test Data Center',
            portrait='http://example.com/portrait.jpg',
            avatar='http://example.com/avatar.jpg',
            background='Test Background',
            personality='Test Personality',
            pronouns='Test Pronouns',
            member=self.member
        )
        self.assertEqual(character.name, 'Test Character')

    def test_unique_character_id(self):
        print("Test uniqueness constraint on character_id")
        character1 = Character.objects.create(
            character_id=1,
            name='Character 1',
            server='Server 1',
            data_center='Data Center 1',
            portrait='http://example.com/portrait1.jpg',
            avatar='http://example.com/avatar1.jpg',
            background='Background 1',
            personality='Personality 1',
            pronouns='Pronouns 1',
            member=self.member
        )
        with self.assertRaises(Exception):
            print("Attempt to create another character with the same character_id should raise an exception")
            character2 = Character.objects.create(
                character_id=1,
                name='Character 2',
                server='Server 2',
                data_center='Data Center 2',
                portrait='http://example.com/portrait2.jpg',
                avatar='http://example.com/avatar2.jpg',
                background='Background 2',
                personality='Personality 2',
                pronouns='Pronouns 2',
                member=self.member
            )

    def test_absolute_url(self):
        print("Test the get_absolute_url")
        character = Character.objects.create(
            character_id=1,
            name='Test Character',
            server='Test Server',
            data_center='Test Data Center',
            portrait='http://example.com/portrait.jpg',
            avatar='http://example.com/avatar.jpg',
            background='Test Background',
            personality='Test Personality',
            pronouns='Test Pronouns',
            member=self.member
        )
        self.assertEqual(character.get_absolute_url(), reverse('character_detail', args=[str(character.name)]))