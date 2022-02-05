from django.test import TestCase
from foods.models import Product, Categorie, ProductReview
from authentication.models import User


class TestUtils(TestCase):

	def setUp(self):
		self.user = User.objects.create(
			username="Toto",
			email="toto@gmail.com",
			password="1234"
			)
		self.cat = Categorie.objects.create(name="Chocolat")
		self.product = Product.objects.create(
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
		nutella = ProductReview.objects.create(
			customer = self.user,
			product_name = self.product,
			rate = 5
		) 
		self.assertEqual(nutella.rate, 5)

