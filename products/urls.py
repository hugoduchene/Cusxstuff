from django.urls import path
from .views import ProductOnly, ProductsHome, ShoppingCart


urlpatterns = [
    path('', ProductsHome.as_view(), name="home_products"),
    path('<int:id_product>/', ProductOnly.as_view(), name="product_only"),
    path('shoppingcart/', ShoppingCart.as_view(), name="shopping_cart")
]
