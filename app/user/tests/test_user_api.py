from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from core.tests.utils import create_test_user

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create')


class UserAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_user(self):
        payload = {
            'email': 'user123@example.com',
            'password': 'user1233',
            'name': 'user',
        }

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        user = get_user_model().objects.get(email=payload['email'])

        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_email_exists(self):
        payload = {
            'email': 'user@example.com',
            'password': 'user123',
            'name': 'user',
        }

        create_test_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_short(self):
        payload = {
            'email': 'user@example.com',
            'password': '123',
            'name': 'user',
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

        user_found = get_user_model().objects.filter(
            email=payload['email']).exists()

        self.assertFalse(user_found)
