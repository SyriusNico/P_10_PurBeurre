from django.db.models import Q
from .models import Product, Favorite
from authentication.models import User


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
				print(objs.category_id)
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

	# New fonctionnality
	def makeANotation(self, choice, mark=int()):
		product = Product.objects.all().filter(product_name__icontains=choice)
		product = product.first()
		if product.notation is not None:
			product.notation += mark
			product.notation = product.notation / 2
			product.save()
		else:
			product.notation = mark 
			product.save()
