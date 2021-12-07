from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from foods.models import Product, Categorie
from foods.views import ResultView


class TestViews(TestCase):

	def setUp(self):
		self.client = Client()
		self.factory = RequestFactory()
		self.product_test = Product.objects.create(
			product_name='test1',
			category_id=Categorie.objects.create(
				name='category_test')
		)
		self.result_test = Product.objects.filter(
			product_name__icontains='test1').first()
		# self.result_url = reverse('result')
		self.detail_url = reverse('detail', args=(self.product_test.id,))

	def test_request_on_result_view(self):
		request = self.factory.get('foods/result/?searched=test1')
		response = ResultView.as_view()(request)
		self.assertEqual(response.status_code, 200)

	def test_product_detail_view_GET(self):
		response = self.client.get(self.detail_url)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'foods/product_detail.html')
