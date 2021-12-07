import requests
from django.db.utils import IntegrityError
from django.core.management.base import BaseCommand
from nutella_project.settings import CATEGORIES_LIST, NB_RESULT
from ...models import Categorie, Product


class OffApi():

	def __init__(self):

		self.url = 'https://fr.openfoodfacts.org/cgi/search.pl'
		self.category = CATEGORIES_LIST
		self.page_size = NB_RESULT

	def payload(self, category):
		payload = {
			'action': 'process',
			'tagtype_0': 'categories',
			'tag_contains_0': 'contains',
			'tag_0': category,
			'tagtype_1': 'nutrition_grade_fr',
			'tag_contains_1': 'contains',
			'page_size': self.page_size,
			'json': 'true',
		}
		return payload


	def getProductsFromOff(self, category):

		payload = self.payload(category)
		req = requests.get(self.url, payload)
		products = req.json().get('products')
		return products

	def _can_be_created(self, product):
		"""
		check if you can register
		its data in your datatabase
		"""
		sugar = "sugars_100g"
		salt = "salt_100g"
		fat = "fat_100g"
		proteins = "proteins_100g"

		if product['nutrition_grade_fr']:
			return True
		if product['product_name']:
			return True
		elif product['product_name'] is not None:
			return True
		elif product['stores'] is not None:
			return True
		elif product[sugar] is not None:
			return True
		else:
			return False

	def storeDatas(self):

		for category in self.category:
			products = self.getProductsFromOff(category)
			categoryData = Categorie.objects.create(name=category)
			try:
				for product in products:				
					if self._can_be_created(product):
						productData = Product( 
							product_name=product.get('product_name'),
							code=product.get('code'),
							nutrition_grade=product.get('nutrition_grade_fr'),
							stores=product.get('stores'),
							link=product.get('url'),
							url=product.get('image_front_url'),
							sugar=product['nutriments'].get('sugars_100g'),
							salt=product['nutriments'].get('salt_100g'),
							fat=product['nutriments'].get('fat_100g'),
							proteins=product['nutriments'].get('proteins_100g'),
							category_id=categoryData
							)
						productData.save()
					else:
					    print("Données incomplètes.")
			except (IntegrityError,KeyError) as e:
				pass

	def deleteDuplicate(self):
		for product in Product.objects.all().reverse():
			if Product.objects.filter(product_name=product.product_name).count() > 1 :
				product.delete()	


class Command(BaseCommand):

	def handle(self, *args, **options):
		offApi = OffApi()
		print("Patientez un instant nous réinitialisations la base de données ...")
		offApi.storeDatas()
		offApi.deleteDuplicate()
		print("Les données ont été ajouté")
