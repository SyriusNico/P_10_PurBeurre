from django.db.models import Q
from .models import Product, Favorite, ProductReview
from authentication.models import User
from django.core.exceptions import ObjectDoesNotExist

class Utils():

	def lookFor(self, product):
		results = Product.objects.filter(product_name__icontains=product)
		result = results.first()
		return result

	def saveMyChoice(self, userId, productToAdd):
		sub = Product.objects.get(product_name=productToAdd)
		favorite = Favorite.objects.create(
			customer=User.objects.get(id=userId),
			favorite=sub
		)

	def giveMeBetterThan(self, product):
		objs = Product.objects.all().filter(product_name__icontains=product)
		objs = objs.first()
		if objs in Product.objects.all():
			try:
				prod = Product.objects.filter(category_id=objs.category_id)
				if objs.nutrition_grade == 'e' or objs.nutrition_grade == 'd':
					sub = prod.filter(
					Q(nutrition_grade='a') | Q(nutrition_grade='b') | Q(nutrition_grade='c')
					)
					return sub
				if objs.nutrition_grade == 'c':
					sub = prod.filter(
					Q(nutrition_grade='a') | Q(nutrition_grade='b')
					)
					return sub
				if objs.nutrition_grade == 'b':
					sub = prod.filter(nutrition_grade='a')
					return sub
				if objs.nutrition_grade == 'a':
					sub = prod.filter(nutrition_grade='a')
					return sub

			except Product.MultipleObjectsReturned:
				pass
		else:
			return None
			

	def addReview(self, user, name):
		productRated = ProductReview.objects.all().filter(
			customer = user,
			product_name = name
		)
		if productRated:
			productRated.delete()
			productReview = ProductReview.objects.create(
				customer = user,
				product_name = name,
			)
			productReview.save()
			reviews = ProductReview.objects.all()
			myReview = reviews.filter(
				customer = user,
				product_name = name
			)
			return myReview
		else:
			productReview = ProductReview.objects.create(
				customer = user,
				product_name = name,
			)
			productReview.save()
			reviews = ProductReview.objects.all()
			myReview = reviews.filter(
				customer = user,
				product_name = name
			)
			return myReview

	def ratingProduct(self, user, name, _rate):
		productReview = ProductReview.objects.get(
			customer =user,
			product_name = name
		)
		productReview.rate = _rate
		productReview.save()
