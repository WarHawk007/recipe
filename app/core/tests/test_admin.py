from django.test import TestCase, Client
from django.urls import reverse
from core.tests.utils import create_test_superuser, create_test_user


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = create_test_superuser('admin@gmail.com', 'admin123')
        self.client.force_login(self.admin_user)
        self.user = create_test_user('user@gmail.com', 'user123', name='user')

    def test_users_list(self):
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.email)
        self.assertContains(res, self.user.name)

    def test_users_change(self):
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_users_create(self):
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
