from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successfully(self):
        """Test creating a new user with email is succesfull"""
        email = 'sharansandhu8399@gmail.com'
        password = 'test1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.check_password(password), email)

    def test_new_user_email_normalized(self):
        """Tests email for a new user is normalized"""

        email = 'sharansandhu8399@gmail.com'
        user = get_user_model().objects.create_user(email, 'test1234')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test1234')

    def test_create_new_superuser(self):
        """Test creating a new super user"""

        user = get_user_model().objects.create_superuser(
            'sharansandhu8399@gmail.com',
            'test1234'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
