from django.db import models
from django.conf import settings


# Create your models here.
class Categorie(models.Model):
	name = models.CharField(max_length=256)

	def __str__(self):
		return self.name


class Product(models.Model):
	product_name = models.CharField(max_length=255)
	code = models.CharField(max_length=255)
	nutrition_grade = models.CharField(max_length=255)
	stores = models.CharField(max_length=255)
	url = models.URLField(max_length=255)
	link = models.CharField(blank=True, max_length=255)
	sugar = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	salt = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	fat = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	proteins = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	category_id = models.ForeignKey(Categorie, on_delete=models.CASCADE)

	def __str__(self):
		return self.product_name


class Favorite(models.Model):
	customer = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		related_name='customer'
	)
	favorite = models.ForeignKey(Product, on_delete=models.CASCADE,
										  related_name='substitute')

	# replace by product
	def __str__(self):
		return f"{self.customer}"
