from django.urls import path
from .views import (
    ResultView, ProductDetailView,
    ProfilePageView,
    FavoritesPageView,
    RatingPageView
)


urlpatterns = [
    path('result/', ResultView.as_view(), name='result'),
    path('result/<int:id>/', ProductDetailView.as_view(), name='detail'),
    path('result/profile', ProfilePageView.as_view(), name='profile'),
    path('result/favorites', FavoritesPageView.as_view(), name='favorites'),
    path('result/<int:id>/rating', RatingPageView.as_view(), name='rating'),
]
