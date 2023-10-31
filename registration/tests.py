from django.test import TestCase
from .models import CustomUser

class CustomUserModelTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'Pauline',
            'email': 'ochiengpakoth@gmail.com',
            'first_name': 'Pauline',
            'last_name': 'Ochieng',
            'password': 'testpassword',
        }

    def test_create_user_with_data(self):
        user = CustomUser.objects.create_user(**self.user_data)
        self.assertEqual(user.username, 'Pauline')
        self.assertEqual(user.email, 'ochiengpakoth@gmail.com')
        self.assertEqual(user.first_name, 'Pauline')
        self.assertEqual(user.last_name, 'Ochieng')
        self.assertTrue(user.check_password('testpassword'))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser_with_data(self):
        admin_user = CustomUser.objects.create_superuser(
            username='AdminUser',
            email='admin@example.com',
            password='adminpassword',
            **self.user_data
        )
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

    def test_user_str_representation(self):
        user = CustomUser.objects.create_user(**self.user_data)
        self.assertEqual(str(user), 'Pauline')

    def test_user_is_active(self):
        user = CustomUser.objects.create_user(**self.user_data)
        self.assertTrue(user.is_active)

    def test_user_is_not_staff(self):
        user = CustomUser.objects.create_user(**self.user_data)
        self.assertFalse(user.is_staff)

    def test_user_is_not_superuser(self):
        user = CustomUser.objects.create_user(**self.user_data)
        self.assertFalse(user.is_superuser)
