from django.test import TestCase
from django.contrib.auth import get_user_model


class UserModel(TestCase):
    def test_create_user_with_email(self):
        email = "farhansaeed@gmail.com"
        password = "password"
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        emails = [
            ["test1@GMAIL.com", "test1@gmail.com"],
            ["Test2@Gmail.com", "Test2@gmail.com"],
            ["TEST3@GMAIL.com", "TEST3@gmail.com"],
            ["test4@gmail.COM", "test4@gmail.com"]
        ]
        password = "password"
        for email, excepted in emails:
            user = get_user_model().objects.create_user(email=email, password=password)
            self.assertEqual(user.email, excepted)
            self.assertTrue(user.check_password(password))

    def test_create_user_without_email_raise(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', '1234')

    def test_create_super_user(self):
        user = get_user_model().objects.create_super_user(
            email='admin@gmail.com',
            password='admin123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
