from django.test import TestCase,Client
from pages.views import IndexView
from django.urls import resolve



class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        resolver = resolve('/')
        self.assertEqual(
            resolver.func.__name__, IndexView.as_view().__name__
        )
        