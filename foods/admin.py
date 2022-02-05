from django.contrib import admin
from .models import Categorie, Product, Favorite, ProductReview


admin.site.register(Categorie)
admin.site.register(Product)
admin.site.register(Favorite)
admin.site.register(ProductReview)
