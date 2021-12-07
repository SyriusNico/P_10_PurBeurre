from django.core.management.base import BaseCommand
from ...models import Categorie, Product, Favorite

def clearDatas():

	Categorie.objects.all().delete()
	Product.objects.all().delete()
	Favorite.objects.all().delete()

class Command(BaseCommand):

	def handle(self, *args, **options):

		clearDatas()
		print("Les données ont été supprimé")