from django.test import TestCase
from foods.models import Product, Categorie
from authentication.models import User


class TestUtils(TestCase):

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

	def test_product_is_rating(self):
		nutella = Product.objects.get(product_name="nutella")
		nutella.notation = 2
		self.assertIsNotNone(nutella.notation)

	def test_product_is_rating_by_one_user(self, mark=5):
		nutella = Product.objects.get(product_name="nutella")
		nutella.notation = None
		if nutella.notation is not None:
			nutella.notation += mark
			nutella.notation = nutella.notation // 2
		else:
			nutella.notation = mark 
		self.assertEqual(nutella.notation, 5)

	def test_product_is_rating_by_many_user(self, product="nutella", mark=5):
		nutella = Product.objects.get(product_name=product)
		nutella.notation = 8
		if nutella.notation is not None:
			nutella.notation += mark
			nutella.notation = nutella.notation // 2
		else:
			nutella.notation = mark 
		self.assertEqual(nutella.notation, 6)
