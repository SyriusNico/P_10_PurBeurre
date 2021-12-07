from django.test import SimpleTestCase
from django.urls import reverse, resolve
from foods.views import (
	ResultView,
	ProductDetailView,
	ProfilePageView,
	FavoritesPageView
)


class TestUrls(SimpleTestCase):

	def test_result_url_resolves(self):
		url = reverse('result')
		self.assertEqual(resolve(url).func.view_class, ResultView)

	def test_detail_url_resolves(self):
		url = reverse('detail', args=[1])
		self.assertEqual(resolve(url).func.view_class, ProductDetailView)

	def test_profile_url_resolves(self):
		url = reverse('profile')
		self.assertEqual(resolve(url).func.view_class, ProfilePageView)

	def test_favorites_url_resolves(self):
		url = reverse('favorites')
		self.assertEqual(resolve(url).func.view_class, FavoritesPageView)
