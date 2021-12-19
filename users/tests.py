from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

from users.forms import CustomUserCreationForm
from users.views import SingupPageView


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='will',
            email='will@gmail.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superwill',
            email='superwill@gmail.com',
            password='testpass123'
        )
        self.assertEqual(admin_user.username, 'superwill')
        self.assertEqual(admin_user.email, 'superwill@gmail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SingupPageTests(TestCase):
    def setUp(self):
        url = reverse('singup')
        self.response = self.client.get(url)

    def test_singup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'singup.html')
        self.assertContains(self.response, 'Sing Up')
        self.assertNotContains(self.response, 'Hi i should not be here')

    def test_singup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_singup_view(self):
        view = resolve('/accounts/singup/')
        self.assertEqual(
            view.func.__name__,SingupPageView.as_view().__name__
        )
