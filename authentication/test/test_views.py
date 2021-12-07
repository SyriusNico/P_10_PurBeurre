from django.test import TestCase, Client
from django.urls import reverse
from authentication.models import User


class UserRegisterViewTest(TestCase):
	def setUp(self):
		self.client = Client()
		self.user = User.objects.create(username='testuser')
		self.user.set_password('secret')
		self.user.save()

	def test_login_view_url(self):
		response = self.client.get(reverse('login'))
		self.assertEqual(response.status_code, 200)

	def test_user_register_view_url(self):
		response = self.client.get(reverse('register'))
		self.assertEqual(response.status_code, 200)

	def test_user_can_login(self):
		response = self.client.login(username='testuser', password='secret')
		self.assertTrue(response)
