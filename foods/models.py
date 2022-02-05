from django.db import models
from django.db.models.query import QuerySet
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.shortcuts import reverse


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

	def get_absolute_url(self):
		return reverse('detail', args=[self.id,])

	def get_rating(self):

		total = sum(review['rate'] for review in self.reviews.values())

		if self.reviews.count() > 0:
			return int(total / self.reviews.count())
		else:
			return 0

	def get_count(self):
		return self.reviews.count()

class Favorite(models.Model):
	customer = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		related_name='customer'
	)
	favorite = models.ForeignKey(Product, on_delete=models.CASCADE,
										  related_name='substitute')

	def __str__(self):
		return f"{self.customer}"


class ProductReview(models.Model):
	customer = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		related_name='reviews'
	)
	product_name = models.ForeignKey(
		Product, on_delete=models.CASCADE,
		related_name='reviews'
	)
	rate = models.IntegerField(default=0)

	def __str__(self):
		return f"{self.product_name}"