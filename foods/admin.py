from django.contrib import admin
from .models import Categorie, Product, Favorite


admin.site.register(Categorie)
admin.site.register(Product)
admin.site.register(Favorite)
