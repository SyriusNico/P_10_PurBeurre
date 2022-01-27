from django.test import TestCase
from foods.models import Product, Categorie


class TestModels(TestCase):

	def setUp(self):
		User.objects.create(
			username="Toto",
			email="toto@gmail.com",
			password="1234"
			)
		Categorie.objects.create(name="Chocolat")
		Product.objects.create(
			product_name="nutella",
			code="123456",
			stores="kekpart",
			url="someurl.com",
			link="somelink",
			sugar=1.3,
			salt=4.2,
			fat=3.3,
			proteins=7.5,
			category_id=Categorie.objects.get(name="Chocolat"),
			)

	def test_product_is_created(self):
		nutella = Product.objects.get(product_name="nutella")
		self.assertIsInstance(nutella, Product)

	def test_user_is_created(self):
		toto = User.objects.get(username="Toto")
		self.assertIsInstance(toto, User)