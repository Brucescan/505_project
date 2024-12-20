from django.urls import path
from .views import ShopListView, ShopDetailView, ShopSearchView, ShopSortedListView

urlpatterns = [
    path('api/shops/', ShopListView.as_view(), name='shop-list'),
    path('api/shop/<int:shop_id>/', ShopDetailView.as_view(), name='shop-detail'),
    path('api/shops/search/', ShopSearchView.as_view(), name='shop-search'),
    path('api/shops/sorted/', ShopSortedListView.as_view(), name='shop-sorted-list'),
]
