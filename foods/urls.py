from django.urls import path
from .views import (
    ResultView, ProductDetailView,
    ProfilePageView,
    FavoritesPageView
)


urlpatterns = [
    path('result/', ResultView.as_view(), name='result'),
    path('result/<int:id>/', ProductDetailView.as_view(), name='detail'),
    path('result/profile', ProfilePageView.as_view(), name='profile'),
    path('result/favorites', FavoritesPageView.as_view(), name='favorites')
]
