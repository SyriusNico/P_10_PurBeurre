from django.test import TestCase, Client
from django.urls import reverse


class TestPagesView(TestCase):

	def setUp(self):
		self.client = Client()
		self.index_url = reverse('index')
		self.legal_url = reverse('legal')

	def test_index_view(self):
		response = self.client.get(self.index_url)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'pages/index.html')

	def test_legal_view(self):
		response = self.client.get(self.legal_url)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'pages/legal.html')
